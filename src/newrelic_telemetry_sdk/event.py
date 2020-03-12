class Event(dict):
    """An event represented in New Relic Insights

    :param event_type: The type of event to report
    :type event_type: str
    """

    def __init__(self, event_type, **kwargs):
        super(Event, self).__init__(eventType=event_type, **kwargs)
