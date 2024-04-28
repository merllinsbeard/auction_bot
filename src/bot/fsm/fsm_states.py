from aiogram.fsm.state import State, StatesGroup

class AdminMenuStates(StatesGroup):
    MENU = State()
    START_AUCTION = State()
    ADDED_CHANNELS = State()
    CHANNEL_IS_CHOISEN = State()
    WAIT_PRIZE_INPUT = State()
    STATISTICS = State()
    
