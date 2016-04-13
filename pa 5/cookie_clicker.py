"""Created on Sun Sep 27 22:03:58 2015

Principles of Computing (Part 1),
programming assignment 5, Cookie Clicker Simulator
https://class.coursera.org/principlescomputing1-004/wiki/view?page=clicker

Author: Sakari Hakala

"""
import math
#import simpleplot
#
## Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
#import matplotlib.pyplot as plt

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 1000000 # use smaller value for testing

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return 'Total: ' + str(self._total_cookies) + '. Cookies: ' + str(self._current_cookies) + '. Time: ' + str(self._current_time) + '. CPS: ' + str(self._current_cps)                
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        cookies_short = cookies - self._current_cookies
        if cookies_short <= 0.0:
            return 0.0
        wait_time = math.ceil(cookies_short / self._current_cps)
        return float(wait_time)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_cookies += time * self._current_cps
            self._total_cookies += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
            self._current_cookies -= cost
            self._current_cps += additional_cps
        
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    info = build_info.clone()
    clicker = ClickerState()
    while clicker.get_time() <= duration:
        time_left = duration - clicker.get_time()
        next_item = strategy(clicker.get_cookies(),clicker.get_cps(), clicker.get_history(),
                             time_left, info)
        if next_item == None:
            break
        time_until = clicker.time_until(info.get_cost(next_item))
        if time_until > time_left:
            break
        clicker.wait(time_until)
        clicker.buy_item(next_item, info.get_cost(next_item), info.get_cps(next_item))
        info.update_item(next_item)
    clicker.wait(time_left)
    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    max_cost = cookies + cps * time_left
    items = build_info.build_items()
    cheapest_item = None
    cheapest_cost = ('inf')
    for item in items:
        cost = build_info.get_cost(item)
        if cost < cheapest_cost and cost <= max_cost:
            cheapest_cost = cost
            cheapest_item = item
    return cheapest_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    max_cost = cookies + cps * time_left
    items = build_info.build_items()
    expensive_item = None
    expensive_cost = (-1)
    for item in items:
        cost = build_info.get_cost(item)
        if cost > expensive_cost and cost <= max_cost:
            expensive_cost = cost
            expensive_item = item
    return expensive_item

#def strategy_best(cookies, cps, history, time_left, build_info):
#    """
#    The best strategy that you are able to implement.
#    """
#    max_cost = cookies + cps * time_left
#    items = build_info.build_items()
#    #print items
#
#    best_item = None
#    best_expected = 0
#    for item in items:
#        cost = build_info.get_cost(item)        
#        cps = build_info.get_cps(item)
#        wait_time = (cost - cookies) / cps
#        #print wait_time
#        if wait_time < 0.0:
#            wait_time = 0.0
#        print time_left - wait_time, cost < max_cost
#        cookies_gain = cps * (time_left - wait_time)
#        if cookies_gain > best_expected and cost < max_cost:
#            best_expected = cookies_gain
#            best_item = item
#    #print history
#    print best_item, cookies, max_cost
#    for item in items:
#        print item, build_info.get_cost(item)
#
#    return best_item
    
def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    max_cost = cookies + cps * time_left
    items = build_info.build_items()
    best_roi_item = None
    best_roi = -1
    for item in items:
        cost = build_info.get_cost(item)
        roi = build_info.get_cps(item) / build_info.get_cost(item)
        if roi >= best_roi and cost <= max_cost:
            best_roi = roi
            best_roi_item = item
    return best_roi_item
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
    #plt.plot(history)
    #plt.show()

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("None", SIM_TIME, strategy_none)
    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    #run_strategy("ROI", SIM_TIME, strategy_roi)
    
#run()
