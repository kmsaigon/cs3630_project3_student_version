"""
CS 3630 Project 3 (Fall 2026): Vacuum Cleaning Robot -- STUDENT FILE

This file is the Fall 2025 notebook's `#export` cells, moved into a module so
that (a) the notebook can `from main import *` and (b) the Webots visualization
can import the same functions live.  Every student TODO keeps its Fall 2025
name, signature, docstring, and marker block.  Provided (non-TODO) code is
carried over verbatim except where noted in instructor/CHANGES_FROM_FALL2025.md.

Layout of this file mirrors the notebook sections:
    3.1  Modeling the State Space           TODO 1-2
    3.2  Probabilistic Outcomes             TODO 3, prob_spec, TODO 4
    3.3  Dynamic Bayes Nets & Sensor Models TODO 5, sensor_spec, TODO 6-12
    3.4  Perception                         create_factor_graph, TODO 13-15
    3.5  Markov Decision Processes          TODO 16-20
"""

import numpy as np
import gtsam
import pandas as pd
import time
import gtbook
from gtbook.display import show
from gtbook.discrete import Variables
VARIABLES = Variables()
def pretty(obj):
    return gtbook.display.pretty(obj, VARIABLES)
def show(obj, **kwargs):
    # Fall 2026: render eagerly so a missing Graphviz `dot` program gives a one-line hint
    # instead of a traceback when Jupyter displays the cell (CHANGES_FROM_FALL2025.md, C3).
    figure = gtbook.display.show(obj, VARIABLES, **kwargs)
    try:
        figure.pipe(format="svg")
    except Exception:
        print("show(): the Graphviz `dot` program was not found, so this diagram is skipped. "
              "It is optional (diagrams are not graded); install it with: conda install -c conda-forge graphviz")
        return None
    return figure

import plotly.express as px


###############################################################################
# Constants. DON'T CHANGE THE VARIABLE NAMES AND VALUES
###############################################################################
ROOMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # choosing to use numbers instead of room names for conciseness, see map above to see what room each number corresponds to
ACTIONS = ["2->1","1->2","2->3","3->2","2->4","4->2","2->5","5->2","2->6","6->7","7->6", "6->2", "2->9", "9->8", "8->9", "9->2"] # these are all the possible actions our robot can take (2 * our total number of doorways!)
LIGHT_LEVELS = ["dark", "medium", "light"] # these are the possible light levels in each room, more on this later


###############################################################################
# Section 3.1: Modeling the State Space
###############################################################################

# TODO 1
def create_action_series(action_variable_char, indices):
    """
    Returns a discrete series of actions

        Parameters:
            character (str): a single character assigned to the action state variable
            indices (list of ints): a list of integer indices

        Returns:
            A (dict): a dictionary with the keys being integer indices and the values
                      being gtsam.DiscreteKeys
    """
    A = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return A


# TODO 2
def create_state_series(state_variable_char, indices):
    """
    Returns a discrete series of rooms

        Parameters:
            character (str): a single character assigned to the room state variable
            indices (list of ints): a list of integer indices

        Returns:
            X (dict): a dictionary with the keys being integer indices and the values
                      being gtsam.DiscreteKeys
    """
    X = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return X


###############################################################################
# Section 3.2: Probabilistic Outcomes
###############################################################################

# TODO 3
def create_motion_model(states, actions, action_spec):
    """
    Returns a motion model that describes state transitions P(X2|X1, A1)

        Parameters:
            states (dict): a discrete series of states (rooms)
            actions (dict): a discrete series of actions
            spec (str): a table that contains all possible values for P(X2|X1, A1)

        Returns:
            motion_model (gtsam.DiscreteConditional): a DiscreteConditional that
            describes the state transition model P(X2|X1, A1)
    """
    motion_model = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return motion_model


# TODO: FILL OUT THE MISSING ELEMENTS IN THE TABLE USING THE PROB_SPEC
# You only have to fill out the transition table for actions 2 -> 1 & 1 -> 2.
# Even within these actions, you only have to fill out the transition probabilities from state 1.

# ACTIONS = ["2->1","1->2","2->3","3->2","2->4","4->2","2->5","5->2","2->6","6->7","7->6", "6->2", "2->9", "9->8", "8->9", "9->2"] # these are all the possible actions our robot can take (2 * our total number of doorways!)

prob_spec = """
    #####   FILL IN THESE TWO      ####### 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0 100/0/0/0/0/0/0/0/0
    93/4/3/0/0/0/0/0/0 0/100/0/0/0/0/0/0/0 3/6/88/3/0/0/0/0/0 0/100/0/0/0/0/0/0/0 0/6/3/87/4/0/0/0/0 0/100/0/0/0/0/0/0/0 0/5/0/2/92/1/0/0/0 0/100/0/0/0/0/0/0/0 0/4/0/0/1/93/2/0/0 0/100/0/0/0/0/0/0/0 0/100/0/0/0/0/0/0/0 0/100/0/0/0/0/0/0/0 0/6/2/0/0/0/0/4/88 0/100/0/0/0/0/0/0/0 0/100/0/0/0/0/0/0/0 0/100/0/0/0/0/0/0/0
    0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 2/90/5/3/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0 0/0/100/0/0/0/0/0/0
    0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/90/2/6/2/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0 0/0/0/100/0/0/0/0/0
    0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/94/0/1/4/1/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0 0/0/0/0/100/0/0/0/0
    0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/5/0/0/0/5/90/0/0 0/0/0/0/0/100/0/0/0 0/94/0/0/0/4/2/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0 0/0/0/0/0/100/0/0/0
    0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/96/4/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0 0/0/0/0/0/0/100/0/0
    0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/100/0 0/0/0/0/0/0/0/7/93 0/0/0/0/0/0/0/100/0
    0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/0/100 0/0/0/0/0/0/0/92/8 0/0/0/0/0/0/0/0/100 0/90/0/0/0/0/0/4/6
"""


# TODO 4
def create_bayes_net(motion_model):
    """
    Returns a discrete bayes net of the motion model P(X2|X1, A1)

        Parameters:
            motion_model (gtsam.DiscreteConditional): a DiscreteConditional that describes the state transition model P(X2|X1, A1)

        Returns:
            bayes_net (gtsam.DiscreteBayesNet): a DiscreteBayesnet that describes the motion model
    """
    bayes_net = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return bayes_net


###############################################################################
# Section 3.3: Dynamic Bayes Nets & Sensor Models
###############################################################################

# TODO 5
def create_sensor_series(sensor_variable_char, indices):
    """
    Returns a discrete series of light levels

        Parameters:
            sensor_variable_char (str): a single character assigned to the light levels state variable
            indices (list of ints): a list of integer indices

        Returns:
            Z (dict): a dictionary with the keys being integer indices and the values
                      being gtsam.DiscreteKeys
    """
    Z = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return Z


# TODO Define the sensor spec, most already filled out, please just fill out the sensor spec for rooms 1 and 2
sensor_spec = """
    15/50/35 20/60/20 15/45/40 20/55/25 20/55/25 20/55/25 20/55/25 40/50/10 60/35/5
"""


#TODO 6
def get_prior():
    """
    Returns the priors to have uniform distribution over all the rooms.

    """
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################
    priors = None
    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return priors


#TODO 7
def get_kitchen_start_prior():
    """
    Change kitchen start prior such that it reflects the knowledge that the robot always starts in the kitchen.

    """
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################
    kitchen_start_prior = None
    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return kitchen_start_prior


#TODO 7
def create_dbn(priors, X, A, Z, sensor_spec, prob_spec, N):
    """
    Return a dynamic bayes net

        Parameters:
            bayes_net (gtsam.DiscreteBayesNet): a discrete bayes net that describes the motion model
            priors (str): the prior knowledge of the robot regards the room state
            X (dict): a discrete series of (room) states
            A (dict): a discrete series of actions
            Z (dict): a discrete series of sensor measurements (light levels)
            sensor_spec (str): A table that contains all possible values of P(Z1|X1)
            prob_spec (str): A table that contains all possible values of P(X2|X1, A1)
            N: number of states for the DBN

        Returns:
            dbn (gtsam.DiscreteBayesNet): the dynamic bayes net that represents the evolution of the (room) state over time
    """
    dbn = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return dbn


#TODO 8
def create_simple_action_sequence(A, num_actions):
    """
    Return an action sequence such that all actions are 3->2 (kitchen to corridor).  This is pretty boring because the robot will not leave the corridor once there.

        Parameters:
            A: Actions dictionary
            num_actions (int): number of actions within the sequence

        Returns:
            action_seq (dict): a dictionary with the key being the action state variable (for instance, "A1", "A2", ...)
                               and the value being the action from "3->2"
    """
    action_seq  = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return action_seq


#TODO 9
def create_custom_action_sequence(A, num_actions):
    """
    Return an action sequence for starting from the kitchen and visiting both of the small offices, and then returning to the kitchen.
    The action cycle should be as follows: 3->2, 2->6, . . . . and so on.  It will be a cycle of 6
    If the number of actions is not a multiple of 6, that is ok, the robot will simply stop afer the last action in whatever state it is in.

        Parameters:
            A: Actions dictionary
            num_actions (int): number of actions within the sequence

        Returns:
            action_seq (dict): a dictionary with the key being the action state variable (for instance, "A1", "A2", ...)
                               and the value being the specific action from "L", "R", "U", "D"
    """
    action_seq  = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return action_seq


#TODO 10
def ancestral_sampling(dbn, action_sequence):
    """
    Returns an ancestral sampling of a dynamic bayes net

        Parameters:
            dbn (gtsam.DiscreteBayesNet): the dynamic bayes net that represents the evolution of the (room) state over time
            action_sequence (dict): a dictionary with the key being the action state variable (for instance, "A1", "A2", ...)
                                    and the value being the specific action from "L", "R", "U", "D"

        Returns:
            samples (gtsam.DiscreteValues): a DiscreteValues variable that contains key-value pairs with the key being all variables
                                            within the dynamic bayes net (for instance X1, X2, A1, A2, Z1, Z2) and the value being
                                            its corresponding sampled value
    """
    samples = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return samples


#TODO 11
def simulate_multiple(dbn, action_sequence, N, K):
    """
    Runs ancestral sampling multiple times and returns the Kth state of each iteration.

        Parameters:
            dbn (gtsam.DiscreteBayesNet): the dynamic bayes net that represents the evolution of the (room) state over time
            action_sequence (dict): a dictionary with the key being the action state variable (for instance, "A1", "A2", ...)
                                    and the value being the specific action from "3->2", "2->6", "6->7", "7->6", "6->2", "2->3"
            N (int): number of times to simulate the dbn
            K (int): which value to return

        Returns:
            resulting_states (list): a list of strings containing the final state of ancestral sampling.
    """
    resulting_states = []
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return resulting_states


#TODO 12
def plot_state_histogram(state_list):
    """
    Plot the graph showing the number of times each state is visited in the list provided.
    Check out https://plotly.com/python/plotly-express/ for more info about using plotly.

    Make sure to include axis titles!

        Parameters:
            state_list (list): the list of visited states

        Returns:
            figure (histogram): the histogram of visited states

    """
    figure = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return figure


###############################################################################
# Section 3.4: Perception
###############################################################################

# Provided.  Builds the HMM factor graph for N states.
#
# Fall 2026 change (see instructor/CHANGES_FROM_FALL2025.md, item C1):
# the Fall 2025 version looped `for k, measurement in enumerate(LIGHT_LEVELS)`,
# which always added exactly three likelihood factors (Z1=dark, Z2=medium,
# Z3=light) no matter what N was, and computed `priors = get_prior()` without
# using it.  The optional keyword arguments below let the Webots MPE mode (and
# the notebook) pass real measurements, actions, and a prior.  With no keyword
# arguments the graph is identical to Fall 2025 for N = 3, and for N > 3 it
# now carries one likelihood factor per state (cycling dark, medium, light)
# instead of factors on X1..X3 only.
def create_factor_graph(N, measurements=None, actions=None, prior=None):
    """
    Returns (graph, X): the HMM factor graph over N room states and its state series.

        Parameters:
            N (int): number of states X1..XN
            measurements (list of str, optional): N light levels from LIGHT_LEVELS, one per state.
                Default: LIGHT_LEVELS[k % 3] for k = 0..N-1 (dark, medium, light, dark, ...).
            actions (list of str, optional): N-1 actions from ACTIONS, one per transition.
                Default: the values of create_custom_action_sequence(A, N-1).
            prior (str, optional): 9-number spec for P(X1). Default: the robot starts in the kitchen.

        Returns:
            graph (gtsam.DiscreteFactorGraph), X (dict): the factor graph and the state series
    """
    X = create_state_series("X", range(1,N+1))
    A = create_action_series("A", range(1,N))
    Z = create_sensor_series("Z", range(1,N+1))
    if actions is None:
        action_assignment = VARIABLES.assignment(create_custom_action_sequence(A, N-1))
    else:
        action_assignment = VARIABLES.assignment({A[k]: actions[k-1] for k in range(1, N)})
    if measurements is None:
        measurements = [LIGHT_LEVELS[k % len(LIGHT_LEVELS)] for k in range(N)]
    if prior is None:
        prior = "0 0 1 0 0 0 0 0 0"
    # A DiscreteFactorGraph prior is a space-separated spec, while the priors
    # returned by get_prior()/get_kitchen_start_prior() are slash-separated
    # DiscreteConditional specs. Accept both.
    prior = prior.replace("/", " ")

    graph = gtsam.DiscreteFactorGraph()
    graph.add(X[1], prior) # \phi(X_1) = P(X_1) # prior
    for k in range(1,N):
        conditional = gtsam.DiscreteConditional(X[k+1], [X[k], A[k]], prob_spec)
        conditional_a_k = conditional.choose(action_assignment) # \phi(X,X+) = P(X+|X,A=a)
        graph.push_back(conditional_a_k)
    for k, measurement in enumerate(measurements):
        conditional = gtsam.DiscreteConditional(Z[k+1], [X[k+1]], sensor_spec)
        z_k = LIGHT_LEVELS.index(measurement)
        factor = conditional.likelihood(z_k) # \phi(X) = P(Z=z|X)
        graph.push_back(factor)
    return graph,X


# Provided.
def generateAllTrajactories(n, X, arr, i, trajectories_list):
    if i == n:
        trajectories_list.append(VARIABLES.assignment({X[k+1]:arr[k] for k in range(n)}))
        return

    for elem in range(9):
        arr[i] = ROOMS[elem]
        generateAllTrajactories(n, X, arr, i + 1,trajectories_list)


#TODO 13
def naive_MPE(graph, N, X):
    """
    Implement the function to return the value for maximum probable explanation and its corresponding state trajectory.
    The naive implementation tries every possible trajectory and selects the one with the highest probability.

      Parameters:
          graph (gtsam.DiscreteFactorGraph): the factor graph used to find mpe
          N: number of states
          X: states dictionary

      Returns:
          mpe_value (float): the value for maximum probable explanation
          mpe_trajectory (gtsam.DiscreteValues): the DiscreteValues variable that contains the key-value pair with the key being the
                                                  (room) state variable and the value being its corresponding value
    """
    mpe_value = 0
    mpe_trajectory = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return mpe_value, mpe_trajectory


#TODO 14
def GTSAM_MPE(graph):
    """
    Implement the function to return the mpe trajectory using gtsam

        Parameters:
            graph (gtsam.DiscreteFactorGraph): the factor graph used to find mpe

        Returns:
            mpe_trajectory (gtsam.DiscreteValues): the DiscreteValues variable that contains the key-value pair with the key being the
                                                   (room) state variable and the value being its corresponding value
    """
    mpe = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return mpe


#TODO 15
def plot_time_complexity():
    """
    Plot the graph to compare the execution time between the naive mpe approach and the gtsam approach
    Check out https://plotly.com/python/plotly-express/ for more info about using plotly.

    X-axis should the N (number states) and Y-axis should be execution time
    """
    figure = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return figure


###############################################################################
# Section 3.5: Markov Decision Processes
###############################################################################

N = 8

def reward_function(state:str, action:str, next_state:str):
    """
    Reward that returns 10 upon entering the Kitchen.
    """
    return 10.0 if next_state == "3" else 0.0

def perform_rollout(markovChain, x1, actions, X):
    """Roll out states given actions as a dictionary"""
    dict = actions.copy()
    dict[X[1]] = x1
    given = VARIABLES.assignment(dict)
    return markovChain.sample(given)

def reward(R, rollout, A, X, k):
    """Return state, action, next_state triple for given rollout at time k."""
    state = rollout[X[k][0]]
    action = rollout[A[k][0]]
    next_state = rollout[X[k+1][0]]
    return R[state, action, next_state]

def rollout_reward(R, rollout, A, X, horizon=N-1, gamma=1.0):
    """Calculate reward for a given rollout"""
    discounted_rewards = [gamma**(k-1) * reward(R, rollout, A, X, k) for k in range(1,horizon)]
    return sum(discounted_rewards)

def get_transition_prob(prob_spec):
    S, U = len(ROOMS), len(ACTIONS)
    conditional = gtsam.DiscreteConditional((2,S), [(0,S), (1,U)], prob_spec)
    T = np.empty((S, U, S), float)
    for assignment, value in conditional.enumerate():
        x, a, y = assignment[0], assignment[1], assignment[2]
        T[x, a, y] = value
    return T


#TODO 16
def create_markovChain(prob_spec, N):
    """
    Implement the function such that it returns a Markov Chain P(X_{t + 1} | X_t, A_t)

        Parameters:
            N (int): number of time steps

        Returns:
            markovChain (gtsam.DiscreteBayesNet): a DiscreteBayeesNet that describes the Markov Chain
    """
    X = VARIABLES.discrete_series("X", range(1, N+1), ROOMS)
    A = VARIABLES.discrete_series("A", range(1, N), ACTIONS)
    markovChain = gtsam.DiscreteBayesNet()
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return markovChain


#TODO 17
def generate_reward_table(prob_spec):
    """
      Generates a reward table using the reward_function.
      Parameters:
              action_spec (str): A table that contains all possible values of P(X2|X1, A1)

      HINT: What does the variable assignment store? How does the dimensionality of the reward table compare to the motion model?
    """
    conditional = gtsam.DiscreteConditional((2,len(ROOMS)), [(0,len(ROOMS)), (1,len(ACTIONS))], prob_spec)
    R = np.empty((len(ROOMS), len(ACTIONS), len(ROOMS)), float)
    for assignment, value in conditional.enumerate():
        ###############################################################################
        #                             START OF YOUR CODE                              #
        ###############################################################################
        pass
        ###############################################################################
        #                              END OF YOUR CODE                               #
        ###############################################################################
    return R


#TODO 18
def control_tape_reward(markovChain, x1, actions, R, A, X):
    """
      Implement the function to calculate the reward given a sequence of actions
      Parameters:
          x1 (str): the initial (room) state
          actions (dict): the dictionary that represents a sequence of actions taken by the agent
          R: array of expected reward given the current state,
    """
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################
    reward = None
    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################

    return reward


#TODO 19
def get_custom_policy():
    # Returns a custom policy that maximizes the expected reward
    #N is the number of actions needed in the policy
    policy = None
    ###############################################################################
    #                             START OF YOUR CODE                              #
    ###############################################################################

    ###############################################################################
    #                              END OF YOUR CODE                               #
    ###############################################################################
    return policy


def get_test_policy():
    # The test policy provides a preferred action from each room
    reasonable_policy = [ACTIONS.index("2->3")] * len(ROOMS)
    return reasonable_policy

def Q_value(R, T, value_function, x, a, gamma=0.9):
    """Calculate Q(x,a) from given value function"""
    return T[x,a] @ (R[x,a] + gamma * value_function)

def calculate_value_system(pi, R, T, gamma=0.9):
    """Calculate A, b matrix of linear system for value computation."""
    b = np.empty((len(ROOMS),), float)
    AA = np.empty((len(ROOMS),len(ROOMS)), float)
    for x, room in enumerate(ROOMS):
        a = pi[x] # action under policy
        b[x] = T[x,a] @ R[x,a] # expected reward under policy pi
        AA[x] = -gamma * T[x,a]
        AA[x,x] += 1
    return AA,b

def calculate_value_function(pi, R,T, gamma=0.9):
    """Calculate value function for given policy"""
    AA, b = calculate_value_system(pi, R,T, gamma)
    return np.linalg.solve(AA,b)


def update_policy(R,T,value_function):
    """Update policy given a value function"""
    new_policy = [None for _ in range(len(ROOMS))]
    for x, room in enumerate(ROOMS):
        Q_values = [Q_value(R, T,value_function, x, a) for a in range(len(ACTIONS))]
        new_policy[x] = np.argmax(Q_values)
    return new_policy


#TODO 20
def policy_iteration(R,T,pi=None, max_iterations=100):
    """Do policy iteration, starting from policy `pi`."""
    for _ in range(max_iterations):
        ###############################################################################
        #                             START OF YOUR CODE                              #
        ###############################################################################
        pass
        ###############################################################################
        #                              END OF YOUR CODE                               #
        ###############################################################################
    raise RuntimeError("No stable policy found after {max_iterations} iterations")
