from maf.maf_file import MafFile


class TestMafFile:
    def test_genes(self):
        genes = MafFile("tests/fixtures/basic.maf").genes

        assert [gene.hugo_symbol for gene in genes] == ["AAA1", "AAA2", "AAA3"]
        assert genes[0].chromosome == "chr1"
