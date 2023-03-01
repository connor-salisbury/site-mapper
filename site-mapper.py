import sys
import logging
import argparse
import os
from pysitemap import crawler

# Define the argument parser
parser = argparse.ArgumentParser(description='Generate a sitemap.xml file for a website.')
parser.add_argument('domain', type=str, help='the domain name of the website to crawl')

# Parse the command-line arguments
args = parser.parse_args()
domain = args.domain

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

        # Define the output file name
        # output_filename = os.path.join('save', domain, 'sitemap.xml')

    # root_url = sys.argv[1]
    root_url = 'https://' + domain
    crawler(root_url, out_file='sitemap.xml')