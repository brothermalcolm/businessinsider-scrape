# businessinsider-scrape

This repository is a one-off project which automatically scrapes a [businessinsider article](http://www.businessinsider.com/asian-hedge-funds-2011-5?IR=T&op=1&r=US&IR=T/#-ht-capital-management-hong-kong-1) for data related to hedge funds in Asia.<P>

The following data is scraped using the Python lxml library which I've found to be the simplest solution to web-scraping a single webpage using HTML/XML and the XPath query language:<P>
Name of Hedge Fund<BR>
Year Founded<BR>
Asset Under Management in US$ (AUM)<BR>
Name of Hedge Fund Manager<BR>
Strategies<BR>

