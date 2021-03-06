import unittest

from universe import engine
from universe import systems


class PopulationTestCase(unittest.TestCase):
    def test_population_growth(self):
        state = {
            'turn': 2500,
            'width': 1000,
            'entities': {
                0: {
                    'type': 'species',
                    'singular_name': 'Human',
                    'plural_name': 'Humans',
                    'growth_rate': 15,
                },
                1: {
                    'type': 'planet',
                    'population': 1000,
                    'x': 480,
                    'y': 235,
                    'owner_id': 0,
                    'queue': [],
                },
            }
        }

        S = engine.GameState(state, {})
        results = S.generate()

        self.assertEqual(results,
                         {'turn': 2501,
                          'width': 1000,
                          'entities': {
                              0: {
                                  'type': 'species',
                                  'singular_name': 'Human',
                                  'plural_name': 'Humans',
                                  'growth_rate': 15,
                                  },
                              1: {
                                  'type': 'planet',
                                  'population': 1150,
                                  'x': 480,
                                  'x_prev': 480,
                                  'y': 235,
                                  'y_prev': 235,
                                  'owner_id': 0,
                                  'queue': [],
                              },
                          }
                         })
