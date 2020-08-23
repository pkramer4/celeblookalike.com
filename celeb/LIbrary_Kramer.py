# Author: Preston Kramer
# Date: 6/26/2020
# Description: Creates Library management system, tracking patrons and items in library


class LibraryItem:
    """
    Represents item available in library
    attribues:
        library_item_id (str): unique id of item
        title (str): title of item
        location (str): item's location: 'ON_SHELF', 'ON_HOLD_SHELF', or 'CHECKED_OUT'
        checked_out_by (Patron): which patron (if any) has checked out item
        requested_by (Patron): which patorn (if any) has requested item
        date_checked_out (int): when item checked out, Library.current_date
    methods:
        get_library_item_id
        get_title
        get_location
        get_checked_out_by
        get_requested_by
        get_date_checked_out
        set_checked_out_by
    """

    def __init__(self, library_item_id, title):
        """
        constructs LibraryItem class
        :param library_item_id (str):
        :param title (str):
        """

        self._library_item_id = library_item_id
        self._title = title
        self._location = 'ON_SHELF'
        self._requested_by = None
        self._checked_out_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """returns LibraryItem library_item_id (str)"""

        return self._library_item_id

    def get_title(self):
        """returns LibraryItem title (str)"""

        return self._title

    def get_location(self):
        """returns LibraryItem location (str)"""

        return self._location

    def get_requested_by(self):
        """returns which patron LibraryItem was requested_by (Patron object or None)"""

        return self._requested_by

    def get_checked_out_by(self):
        """returns LibraryItem checked_out_by (Patron)"""

        return self._checked_out_by

    def get_date_checked_out(self):
        """returns LibraryItem date_checked_out (int)"""

        return self._date_checked_out

    def set_checked_out_by(self, patron):
        """
        updates which patron has checked out item
        parameters:
            patron (Patron): patron who checked out book
        """

        self._checked_out_by = patron

    def set_date_checked_out(self, date):
        """
        updates the date that item was checked out
        parameters:
            date (int): day since library opening that item was checked out
        """

        self._date_checked_out = date

    def set_location(self, new_location):
        """
        updates item's location
        parameters:
            new_location (str): new location of item
        """

        self._location = new_location

    def set_requested_by(self, request_patron):
        """
        updates which Patron has requested LibraryItem object
        parameters:
            request_patron (Patron): patron requesting LibraryItem
        """

        self._requested_by = request_patron


class Book(LibraryItem):
    """
    represents Book in library, inherits from LibraryItem class
    attributes:
        all attributes inherited from LibraryItem class
        author (str)
        check_out_length (int): number of days book may be checked out
    methods:
        all methods inherited from LibraryItem class
        get_check_out_length
        get_author
    """

    def __init__(self, library_item_id, title, author):
        """
        constructs Book object, inheriting attributes from LibraryItem
        Parameters:
            author (str): author of book
        """
        super().__init__(library_item_id,title)

        self._author = author
        self._check_out_length = 21

    def get_check_out_length(self):
        """returns check_out_length of book (int)"""

        return self._check_out_length

    def get_author(self):
        """returns book's author"""

        return self._author


class Movie(LibraryItem):
    """
    represents Movie in library, inherits from LibraryItem class
    attributes:
        all attributes inherited from LibraryItem class
        director (str)
        check_out_length (int): number of days movie may be checked out
    methods:
        all methods inherited from LibraryItem class
        get_check_out_length
        get_director
    """

    def __init__(self, library_item_id, title, director):
        """
        constructs Movie object, inheriting attributes from LibraryItem
        Parameters:
            director (str): director of movie
        """
        super().__init__(library_item_id, title)

        self._director = director
        self._check_out_length = 7

    def get_check_out_length(self):
        """returns check_out_length of movie (int)"""

        return self._check_out_length

    def get_director(self):
        """returns Movie's director"""

        return self._director


class Album(LibraryItem):
    """
    represents Album in library, inherits from LibraryItem class
    attributes:
        all attributes inherited from LibraryItem class
        artist (str)
        check_out_length (int): number of days album may be checked out
    methods:
        all methods inherited from LibraryItem class
        get_check_out_length
        get_artist
    """

    def __init__(self, library_item_id, title, artist):
        """
        constructs Album object, inheriting attributes from LibraryItem
        Parameters:
            artist (str): artist of album
        """
        super().__init__(library_item_id,title)

        self._artist = artist
        self._check_out_length = 14

    def get_check_out_length(self):
        """returns check_out_length of Album (int)"""

        return self._check_out_length

    def get_artist(self):
        """returns album's artist"""

        return self._artist


class Patron:
    """
    represents patron of library
    Attributes:
        patron_id (str): patron's unique identifier
        name (str): name of patron
        checked_out_items (dict): items checked out by patron and their id ({item: item id})
        fine_amount (float): amount patron owes in fines
    Methods:
        get_patron_id
        get_name
        get_checked_out_items
        get_fine_amount
        add_library_item
        remove_library_item
        amend_fine
    """

    def __init__(self, patron_id, name):
        """
        constructs Patron object
        Parameters:
            patron_id (str): patron's unique id
            name (str): patron's unique name
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = {}
        self._fine_amount = 0

    def get_patron_id(self):
        """returns Patron's id value"""

        return self._patron_id

    def get_name(self):
        """return's Patron's name"""

        return self._name

    def get_checked_out_items(self):
        """returns checked_out_items dictionary"""

        return self._checked_out_items

    def get_fine_amount(self):
        """returns fines owed by Patron"""

        return self._fine_amount

    def add_library_item(self, item):
        """
        adds given library item to checked_out_items dictionary
        key:value pair = {item: item id}
        parameters:
            item (LibraryItem): item to be checked out
        """

        self._checked_out_items[item] = item.get_library_item_id()

    def remove_library_item(self, item):
        """
        removes given item from Patron's checked out items
        parameters:
            item (LibraryItem): item to be removed from checked_out_items
        """
        # prevents KeyError if item not in dict: removes item if in dictionary: if not, passes on
        try:
            del self._checked_out_items[item]

        except:
            pass

    def amend_fine(self, amendment):
        """
        changes the value of the fine amount owed by the given amendment, can be positive or negative
        Parameters:
            amendment (float/int): amount added/subtracted to fine_amount
        """

        self._fine_amount = self._fine_amount + amendment


class Library:
    """
    Represents Library object with items and patrons
    attribues:
        holdings (dict): what LibraryItems library holds and their id
        members (dict): Patrons who are members of library and their id
        current_date (int): Days from library opening
    methods:
        add_library_item
        add_patron
        get_library_item_from_id
        get_patron_from_id
        check_out_library_item
        return_library_item
        request_library_item
        pay_fine
        increment_current_date
    """

    def __init__(self):
        """constructs Library object"""

        # represents date from library opening
        self._current_date = 0

        self._holdings = {}
        self._members = {}

    def add_library_item(self, item):
        """
        adds given item to library holdings dictionary ({item id: item})
        parameters:
            item (LibraryItem): Library Item to be added to holdings
        """

        self._holdings[item.get_library_item_id()] = item

    def add_patron(self, patron):
        """
        adds given Patron to library membership dictionary ({member id: member})
        parameters:
            item (LibraryItem): Library Item to be added to holdings
        """

        self._members[patron.get_patron_id()] = patron

    def get_library_item_from_id(self, item_id):
        """
        Returns LibraryItem associated with given ID if item is in holdings
        Parameters:
             item_id (str):
        Returns:
            LibraryItem associated with id if present in holdings
            None if id not in holdings
        """

        try:
            return self._holdings[item_id]
        except:
            return None

    def get_patron_from_id(self, patron_id):
        """
        Returns Patron associated with given ID if patron is in members
        Parameters:
             patron_id (str):
        Returns:
            Patron associated with id if present in holdings
            None if id not in members
        """

        try:
            return self._members[patron_id]
        except:
            return None

    def get_current_date(self):
        """returns the current dat of library item (int)"""

        return self._current_date

    def get_holdings(self):
        """returns library holdings (dictionary)"""

        return self._holdings

    def get_members(self):
        """returns library members dictionary"""

        return self._members

    def check_out_library_item(self, patron_id, item_id):
        """
        checks out an item for a patron
        updates item requested_by, date_checked_out, location
        updates Patron's checked_out_items
        parameters:
            patron_id (str): Patron of interest's id
            item_id (str): LibraryItem of interest's id
        returns:
            'patron not found' if id not in members
            'item not found' if item not in holdings
            'item already checked out' if item location is checked out
            'item on hold by another patron' if item already reserved
            'check out successful' if item added to patron's checked out items
        """

        # gets Patron object from members dictionary given member id, prevents KeyError
        try:
            check_out_patron = self._members[patron_id]

            # gets LibraryItem object from holdings dictionary given item id, prevents KeyError
            try:
                item = self._holdings[item_id]

                if item.get_location() == 'CHECKED_OUT':
                    return 'item already checked out'

                # if item is on hold by anyone other than check_out_patron, return on hold by other patorn
                elif item.get_location() == 'ON_HOLD_SHELF' and item.get_requested_by() != check_out_patron:
                    return 'item on hold by other patron'

                else:

                    item.set_checked_out_by(check_out_patron)
                    item.set_date_checked_out(self._current_date)
                    item.set_location('CHECKED_OUT')
                    item.set_requested_by(None)

                    check_out_patron.add_library_item(item)

                    return 'check out successful'

            # if item id not in Library holdings
            except KeyError:
                return 'item not found'

        # if patron not in library members
        except KeyError:
            return 'patron not found'

    def request_library_item(self, patron_id, item_id):
        """
        updates that patron that has requested item or shows if item already requested
         parameters:
            patron_id (str): Patron of interest's id
            item_id (str): LibraryItem of interest's id
        return:
            'patron not found' if id not in members
            'item not found' if item not in holdings
            'item already on hold' if item already requested
            'request successful' if item's requested_by updated successfully
        """

        # gets Patron object from members dictionary given member id, prevents KeyError
        try:
            request_patron = self._members[patron_id]

            # gets LibraryItem object from holdings dictionary given item id, prevents KeyError
            try:
                item = self._holdings[item_id]

                if item.get_requested_by() != None:
                    return 'item already on hold'

                else:
                    item.set_requested_by(request_patron)

                    # move item to hold shelf if requested and not checked out
                    if item.get_location() == 'ON_SHELF':
                        item.set_location('ON_HOLD_SHELF')

                    return 'request successful'

            # if item id not in Library holdings
            except KeyError:
                return 'item not found'

        # if patron not in library members
        except KeyError:
            return 'patron not found'

    def return_library_item(self, item_id):
        """
        returns item to library holdings if item not already on shelf
        updates item's location to shelf if not requested or on hold shelf if requested'
        updates Patron's checked_out_items
        parameters:
            item_id (str): LibraryItem of interest's id
        returns:
            'item not found' if item not in holdings
            'item already in library' if item on shelf or hold shelf
            'return successful' if item successfully put back on library shelf
        """

        # gets LibraryItem object from holdings dictionary given item id, prevents KeyError
        try:
            item = self._holdings[item_id]

            if item.get_location() != 'CHECKED_OUT':
                return 'item already in library'

            else:

                # gets patron that checked out item and removes item from what they've checked out
                check_out_patron = item.get_checked_out_by()
                check_out_patron.remove_library_item(item)

                # if item requested by someone, put on hold shelf, else put on regular shelf
                if item.get_requested_by() != None:
                    item.set_location('ON_HOLD_SHELF')

                else:
                    item.set_location('ON_SHELF')

                return 'return successful'

        # if item id not in Library holdings
        except KeyError:
            return 'item not found'


    def pay_fine(self, patron_id, fine_payment):
        """
        pay's a specified amount of a patron's fines owed to library
        """
        try:
            request_patron = self._members[patron_id]

            request_patron.amend_fine((-1 * fine_payment))

            return 'payment successful'

        # if patron not in library members
        except KeyError:
            return 'patron not found'

    def increment_current_date(self):
        """
        increases the current library date by one day
        adds fines (0.1, ten cents) to all patrons with overdue checked out items
        """
        self._current_date += 1

        for library_item in self._holdings.values():

            if library_item.get_location() == 'CHECKED_OUT':

                increment_patron = library_item.get_checked_out_by()

                # if the item has been checked out longer than the allowed check out length, add fines
                if (self._current_date - library_item.get_date_checked_out()) > library_item.get_check_out_length():

                    increment_patron.amend_fine(0.1)
