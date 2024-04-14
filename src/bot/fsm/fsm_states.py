from aiogram.fsm.state import State, StatesGroup

class AdminMenuStates(StatesGroup):
    start = State()
    mainmenu = State()
    channels = State()
    statistics = State()
    
