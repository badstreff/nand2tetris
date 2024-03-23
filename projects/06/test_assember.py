import assembler
import io


class TestAssembler:
    def test_preprocess(self):
        test_data = """
            // some initial text data
            @1000
            // another commont
            @symbol
            @symbol2    // with whitespace and comment
            (LABEL1)
            D=A
            @3000
            (LABEL2)
            D=A
        """
        f = io.StringIO(test_data)
        print(f)
        st = assembler.SymbolTable()
        asm = assembler.Assembler(src=f, st=st)
        asm.preprocess()
        assert len(asm.program) == 6
        assert "symbol" in asm.st
        assert isinstance(st["symbol"], int)
        assert "symbol2" in asm.st
        assert isinstance(st["symbol2"], int)
        assert st["R0"] == 0 # test we did not reset a 'falsy' value
        assert "symbol3" not in st
        assert st["LABEL1"] == 3
        assert st["LABEL2"] == 5
        assert st["symbol"] == 16
        assert st["symbol2"] == 17


class TestParser:
    def test_ainstruction(self):
        tests = [
            {"instruction": "@symbol", "value": "symbol", "binary": None},
            {"instruction": "@123456", "value": "123456", "binary": "11110001001000000"},
        ]
        for t in tests:
            ins = t["instruction"]
            parsed = assembler.Parser.parse(ins)
            assert isinstance(parsed, assembler.AInstruction)
            assert parsed.value == t["value"]
            assert parsed.tobinary() == t["binary"]

    def test_cinstruction(self):
        tests = [
            {"instruction": "D=A", "dest": "D", "comp": "A", "jump": None, "binary": "1110110000010000"},
            {"instruction": "D=M", "dest": "D", "comp": "M", "jump": None, "binary": "1111110000010000"},
            {"instruction": "D;JLE", "dest": None, "comp": "D", "jump": "JLE", "binary": "1110001100000110"},
            {"instruction": "0;JMP", "dest": None, "comp": "0", "jump": "JMP", "binary": "1110101010000111"},
   
        ]
        for t in tests:
            ins = t["instruction"]
            parsed = assembler.Parser.parse(ins)
            print(parsed)
            assert isinstance(parsed, assembler.CInstruction)
            assert parsed.dest == t["dest"]
            assert parsed.comp == t["comp"]
            assert parsed.jump == t["jump"]
            assert parsed.tobinary() == t["binary"]