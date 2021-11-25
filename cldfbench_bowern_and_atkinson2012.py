import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bowern_and_atkinson2012"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('bowern_and_atkinson2011.mcct.trees'),
            self.metadata,
            args.log)
