from aiogram.fsm.state import State, StatesGroup

class AdminMenuStates(StatesGroup):
    MENU = State()
    START_AUCTION = State()
    ADDED_CHANNELS = State()
    STATISTICS = State()
    
