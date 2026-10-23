"""A simple bag-of-words model for measuring document-query similarity."""

from .files import get_paths
from .text import txt_terms, load_terms, unique_entries, vocabulary
from .vectors import vector, binary_ttd_vector, ttd
from .distance import e_distance, min_dis