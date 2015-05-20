#!/usr/bin/python

# GPIO capteur ultrason avant
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Delais entre 2 mesure d'un capteur ultrason
DELAY_MESURE = 0.05

# Delais entre 2 commandes de la PO
DELAY_CMD_PO = 0.01

# Parametres servoblaster
DEV_DIRECTION = 'P1-12'     # Identifiant servo-moteur de direction
DEV_VITESSE = 'P1-11'       # Identifiant variateur de vitesse
GPIO_DIRECTION = 12         # Numero identifiant servo-moteur rirection (GPIO18)
GPIO_VITESSE = 11           # Numero identifiant variateur de vitesse (GPIO17)
MIN_US_SB = 1000            # Largeur d'impultion MINimale en us
MAX_US_SB = 2000            # Largeur d'impultion MAXimale en us

# Adresse IP d'ecoute du serveur TCP
BIND_IP = 192.168.1.95
# Port d'ecoute du serveur TCP
CLIENT_TCP_PORT = 10200
# Taille du buffer de reception TCP
CLIENT_TCP_BUFFER_SIZE = 1024

# Configuration module Xbee
XBEE_DIR = '/dev/tty.usbserial-DA01A8AG' # Chemin module Xbee
XBEE_BAUD = 115200
XBEE_TIMEOUT = 1
