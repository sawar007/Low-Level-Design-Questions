class Node:
    """
    Node class represents a node in a doubly-linked list.
    Each node contains data (URL), a reference to the next node, and a reference to the previous node.
    """

    def __init__(self, url):
        """
        Initializes a new Node with the given URL.

        Parameters:
        - url (str): The URL associated with the node.
        """
        self.data = url
        self.next = None
        self.prev = None


class Browser:
    """
    Browser class represents a basic browser history using a doubly-linked list of URLs.
    The Browser allows users to visit URLs, navigate forward, navigate backward, and display the current URL.
    """

    def __init__(self, homepage):
        """
        Initializes a new Browser with a specified homepage.

        Parameters:
        - homepage (str): The initial homepage URL.
        """
        self.current = Node(homepage)
        print(f'Now Browser is at {self.current.data}')

    def visit(self, url):
        """
        Visits a new URL, adding it to the browser history.

        Parameters:
        - url (str): The URL to visit.
        """
        print(f'Visiting {url} ...')
        node = Node(url)
        self.current.next = node
        node.prev = self.current
        self.current = node
        print(f'Now Browser is at {self.current.data}')

    def forward(self):
        """
        Navigates forward in the browser history.
        """
        print('Going Forward ...')
        if self.current.next:
            self.current = self.current.next
        print(f'Now Browser is at {self.current.data}')

    def back(self):
        """
        Navigates backward in the browser history.
        """
        print('Going Back ...')
        if self.current.prev:
            self.current = self.current.prev
        print(f'Now Browser is at {self.current.data}')


# Example usage
browser = Browser('google')
browser.visit('fb')
browser.visit('gmail')
browser.back()
browser.visit('lc')
browser.back()
browser.back()
browser.back()
