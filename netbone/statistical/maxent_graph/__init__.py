__version__ = "0.2.0"

import jax

# ensure jax is using doubles. important.
jax.config.update("jax_enable_x64", True)

from .ecm import ECM

# from .bicm import BICM
# from .biecm import BIECM
# from .bwcm import BWCM
# from .decm import DECM
# from .rcm import RCM