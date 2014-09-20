'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import re
import configparser

class Config:
    def loadConfig(self, configFilename = '../config/sorter.ini'):
        # Load settings from config file
        configReader = configparser.ConfigParser()
        configReader.read(configFilename)
        
        sections = configReader.sections()
        if len(sections) > 0:
            options = configReader.options(sections[0])
            print(options)
            if 'Clutter' in options:
                self.ClutterDir = c[section[0]]['Clutter']
            if 'Movies' in options:
                self.MoviesDir = c[section[0]]['Movies']
            if 'TV' in options:
                self.TvDir = c[section[0]]['TV']
            
    def __init__(self, **kwargs):
        if 'config' in list(kwargs.keys()):
            self.loadConfig(kwargs['config'])
        else:
            # Load from default config
            self.loadConfig()
        # Where the mess is
        if 'clutter' in list(kwargs.keys()):
            self.ClutterDir = kwargs['clutter']
        
        # Where the videos will be neatly arranged
        if 'movies' in list(kwargs.keys()):
            self.MoviesDir = kwargs['movies']
        if 'tv' in list(kwargs.keys()):
            self.TvDir = kwargs['tv']
        
        # Known movie extensions
        self.MovieExtensions = ['.mp4', '.avi', '.mkv']
        
        # Known tv names patterns
        self.TvEpsPattern = '.+\\.S[0-9][0-9](E[0-9][0-9])?\.?.*'
        self.TvEpsRegex = re.compile(self.TvEpsPattern)
        
        #TODO: Known movies patterns
        #self.MoviePattern = ''
        
        # Folders/files to skip
        self.SkipList = ['.AppleDouble']
        
        # Debugging
        self.Debug = False
        
        # Don't execute folder moves
        self.DryRun = False
