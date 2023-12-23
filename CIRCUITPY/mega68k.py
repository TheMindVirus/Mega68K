# Adafruit Grand Central (Beta Edition) # MEGA68K Shield with Motorola MC68010 Pinout #

import board, digitalio

pinout = \
{
    0x0000: { "name": "MEGA68K_CLK",    "pin": board.D52        },
    0x0001: { "name": "MEGA68K_FC0",    "pin": board.A15        },
    0x0002: { "name": "MEGA68K_FC1",    "pin": board.A14        },
    0x0003: { "name": "MEGA68K_FC2",    "pin": board.A13        },

    0x0004: { "name": "MEGA68K_BERR",   "pin": board.D13        },
    0x0005: { "name": "MEGA68K_RESET",  "pin": board.A9         },
    0x0006: { "name": "MEGA68K_HALT",   "pin": board.A8         },

    0x0007: { "name": "MEGA68K_VPA",    "pin": board.A7         },
    0x0008: { "name": "MEGA68K_E",      "pin": board.A6         },
    0x0009: { "name": "MEGA68K_VMA",    "pin": board.A5         },

    0x000A: { "name": "MEGA68K_BR",     "pin": board.D53        },
    0x000B: { "name": "MEGA68K_BG",     "pin": board.D51        },
    0x000C: { "name": "MEGA68K_BGACK",  "pin": board.D50        },
    0x000D: { "name": "MEGA68K_DTACK",  "pin": board.D48        },

    0x000E: { "name": "MEGA68K_AS",     "pin": board.D45        },
    0x000F: { "name": "MEGA68K_RW",     "pin": board.D49        },
    0x0010: { "name": "MEGA68K_UDS",    "pin": board.D47        },
    0x0011: { "name": "MEGA68K_LDS",    "pin": board.D46        },

    0x0012: { "name": "MEGA68K_PL0",    "pin": board.A12        },
    0x0013: { "name": "MEGA68K_PL1",    "pin": board.A11        },
    0x0014: { "name": "MEGA68K_PL2",    "pin": board.A10        },

    0x0015: { "name": "MEGA68K_A1",     "pin": board.D44        },
    0x0016: { "name": "MEGA68K_A2",     "pin": board.D43        },
    0x0017: { "name": "MEGA68K_A3",     "pin": board.D42        },
    0x0018: { "name": "MEGA68K_A4",     "pin": board.D41        },
    0x0019: { "name": "MEGA68K_A5",     "pin": board.D40        },
    0x001A: { "name": "MEGA68K_A6",     "pin": board.D39        },
    0x001B: { "name": "MEGA68K_A7",     "pin": board.D38        },
    0x001C: { "name": "MEGA68K_A8",     "pin": board.D37        },
    0x001D: { "name": "MEGA68K_A9",     "pin": board.D36        },
    0x001E: { "name": "MEGA68K_A10",    "pin": board.D35        },
    0x001F: { "name": "MEGA68K_A11",    "pin": board.D34        },
    0x0020: { "name": "MEGA68K_A12",    "pin": board.D33        },
    0x0021: { "name": "MEGA68K_A13",    "pin": board.D32        },
    0x0022: { "name": "MEGA68K_A14",    "pin": board.D31        },
    0x0023: { "name": "MEGA68K_A15",    "pin": board.D30        },
    0x0024: { "name": "MEGA68K_A16",    "pin": board.D29        },
    0x0025: { "name": "MEGA68K_A17",    "pin": board.D28        },
    0x0026: { "name": "MEGA68K_A18",    "pin": board.D27        },
    0x0027: { "name": "MEGA68K_A19",    "pin": board.D26        },
    0x0028: { "name": "MEGA68K_A20",    "pin": board.D25        },
    0x0029: { "name": "MEGA68K_A21",    "pin": board.D24        },
    0x002A: { "name": "MEGA68K_A22",    "pin": board.D23        },
    0x002B: { "name": "MEGA68K_A23",    "pin": board.D22        },

    0x002C: { "name": "MEGA68K_D0",     "pin": board.A4         },
    0x002D: { "name": "MEGA68K_D1",     "pin": board.A3         },
    0x002E: { "name": "MEGA68K_D2",     "pin": board.A2         },
    0x002F: { "name": "MEGA68K_D3",     "pin": board.A1         },
    0x0030: { "name": "MEGA68K_D4",     "pin": board.A0         },
    0x0031: { "name": "MEGA68K_D5",     "pin": board.D12        },
    0x0032: { "name": "MEGA68K_D6",     "pin": board.D11        },
    0x0033: { "name": "MEGA68K_D7",     "pin": board.D10        },
    0x0034: { "name": "MEGA68K_D8",     "pin": board.D9         },
    0x0035: { "name": "MEGA68K_D9",     "pin": board.D8         },
    0x0036: { "name": "MEGA68K_D10",    "pin": board.D7         },
    0x0037: { "name": "MEGA68K_D11",    "pin": board.D6         },
    0x0038: { "name": "MEGA68K_D12",    "pin": board.D5         },
    0x0039: { "name": "MEGA68K_D13",    "pin": board.D4         },
    0x0040: { "name": "MEGA68K_D14",    "pin": board.D3         },
    0x0041: { "name": "MEGA68K_D15",    "pin": board.D2         },
}

pins = dict()

def setup():
    global pinout, pins
    for key in pinout.keys():
        pins[pinout[key]["name"]] = digitalio.DigitalInOut(pinout[key]["pin"])

def loop():
    global pinout, pins
    for key in pinout.keys():
        print(1 if pins[pinout[key]["name"]].value else 0, ",", pinout[key]["name"])