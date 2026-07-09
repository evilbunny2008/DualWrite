import weewx
from weewx.engine import StdService

class DualWrite(StdService):
    """Mirror each archive record into a second database binding."""

    def __init__(self, engine, config_dict):
        super(DualWrite, self).__init__(engine, config_dict)
        self.binding = 'wx_binding_sqlite'
        # Get (and cache) a manager for the second binding
        self.dbm = engine.db_binder.get_manager(data_binding=self.binding, initialize=True)
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)

    def new_archive_record(self, event):
        self.dbm.addRecord(event.record)
