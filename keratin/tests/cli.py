import os
import unittest

# Define paths to real world-like test sites of varying types.
TEST_SITE_ROOT = os.path.join(os.path.dirname(__file__), 'test_sites')
SITE_SOURCE_DIRS = {
    # No content to process, let through as-is
    'passthrough': os.path.join(TEST_SITE_ROOT, 'passthrough'),
    # Trivial amount of processable content
    'minimal': os.path.join(TEST_SITE_ROOT, 'minimal'),
    # Could be a small, non-blog real world site
    'simplistic': os.path.join(TEST_SITE_ROOT, 'simplistic'),
    # Like 'simplistic', but add the basic post parsing machinery
    'simple_blog': os.path.join(TEST_SITE_ROOT, 'simple_blog'),
    # Complicated stuff to exercise the full power of Keratin
    'complex_blog': os.path.join(TEST_SITE_ROOT, 'complex_blog'),
}

class SiteSkeletonTests(unittest.TestCase):
    pass


class NewPostCreationTests(unittest.TestCase):
    pass
