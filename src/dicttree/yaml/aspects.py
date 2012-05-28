import yaml as yamllib

from metachao import aspect
from metachao.aspect import Aspect

from dicttree.yaml.log import logger as log


class yaml(Aspect):
    """serialize/deserialize a dicttree to/from yaml
    """
    def load(self, stream=None):
        # XXX: can we tell yaml to deserialize into a root node and
        # define a factory for nodes?
        tree = yamllib.load(stream)
        def _load(src, tgt):
            for k,v in src.items():
                if k.endswith('@'):
                    tgt.attrs[k[:-1]] = v
                    log.debug('Set attribute %r: %r' % (k[:-1], v))
                else:
                    self[k] = self.__metachao_class__
                    log.debug('Created node for %r: %r' % (k, v))
                    _load(v, self[k])
        _load(tree, self)

    # def dump(self, stream=None):
    #     return yamllib.dump(self, stream)
