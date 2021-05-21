//Motorola Mega 68010 Pinout

#define SIG_CLK     52
#define SIG_FC0     A15
#define SIG_FC1     A14
#define SIG_FC2     A13

#define SIG_BERR    13
#define SIG_RESET   A9
#define SIG_HALT    A8

#define SIG_VPA     A7
#define SIG_E       A6
#define SIG_VMA     A5

#define SIG_BR      53
#define SIG_BG      51
#define SIG_BGACK   50
#define SIG_DTACK   48

#define SIG_AS      45
#define SIG_RW      49
#define SIG_UDS     47
#define SIG_LDS     46

#define SIG_PL0     A12
#define SIG_PL1     A11
#define SIG_PL2     A10

#define SIG_A1      44
#define SIG_A2      43
#define SIG_A3      42
#define SIG_A4      41
#define SIG_A5      40
#define SIG_A6      39
#define SIG_A7      38
#define SIG_A8      37
#define SIG_A9      36
#define SIG_A10     35
#define SIG_A11     34 
#define SIG_A12     33
#define SIG_A13     32
#define SIG_A14     31
#define SIG_A15     30
#define SIG_A16     29
#define SIG_A17     28
#define SIG_A18     27
#define SIG_A19     26
#define SIG_A20     25
#define SIG_A21     24
#define SIG_A22     23
#define SIG_A23     22

#define SIG_D0      A4
#define SIG_D1      A3
#define SIG_D2      A2
#define SIG_D3      A1
#define SIG_D4      A0
#define SIG_D5      12
#define SIG_D6      11
#define SIG_D7      10
#define SIG_D8      9
#define SIG_D9      8
#define SIG_D10     7
#define SIG_D11     6
#define SIG_D12     5
#define SIG_D13     4
#define SIG_D14     3
#define SIG_D15     2

const int pins[] = 
{
    SIG_CLK, SIG_FC0, SIG_FC1, SIG_FC2,
    SIG_BERR, SIG_RESET, SIG_HALT,
    SIG_VPA, SIG_E, SIG_VMA,
    SIG_BR, SIG_BG, SIG_BGACK, SIG_DTACK,
    SIG_AS, SIG_RW, SIG_UDS, SIG_LDS,
    SIG_PL0, SIG_PL1, SIG_PL2,
    SIG_A1, SIG_A2, SIG_A3, SIG_A4, SIG_A5,
    SIG_A6, SIG_A7, SIG_A8, SIG_A9, SIG_A10,
    SIG_A11, SIG_A12, SIG_A13, SIG_A14, SIG_A15,
    SIG_A16, SIG_A17, SIG_A18, SIG_A19, SIG_A20,
    SIG_A21, SIG_A22, SIG_A23,
    SIG_D0, SIG_D1, SIG_D2, SIG_D3, SIG_D4, SIG_D5,
    SIG_D6, SIG_D7, SIG_D8, SIG_D9, SIG_D10,
    SIG_D11, SIG_D12, SIG_D13, SIG_D14, SIG_D15
};
const size_t szPins = sizeof(pins) / sizeof(int);

const char* names[] = 
{
    "SIG_CLK", "SIG_FC0", "SIG_FC1", "SIG_FC2",
    "SIG_BERR", "SIG_RESET", "SIG_HALT",
    "SIG_VPA", "SIG_E", "SIG_VMA",
    "SIG_BR", "SIG_BG", "SIG_BGACK", "SIG_DTACK",
    "SIG_AS", "SIG_RW", "SIG_UDS", "SIG_LDS",
    "SIG_PL0", "SIG_PL1", "SIG_PL2",
    "SIG_A1", "SIG_A2", "SIG_A3", "SIG_A4", "SIG_A5",
    "SIG_A6", "SIG_A7", "SIG_A8", "SIG_A9", "SIG_A10",
    "SIG_A11", "SIG_A12", "SIG_A13", "SIG_A14", "SIG_A15",
    "SIG_A16", "SIG_A17", "SIG_A18", "SIG_A19", "SIG_A20",
    "SIG_A21", "SIG_A22", "SIG_A23",
    "SIG_D0", "SIG_D1", "SIG_D2", "SIG_D3", "SIG_D4", "SIG_D5",
    "SIG_D6", "SIG_D7", "SIG_D8", "SIG_D9", "SIG_D10",
    "SIG_D11", "SIG_D12", "SIG_D13", "SIG_D14", "SIG_D15"
};
const size_t szNames = sizeof(names) / sizeof(char*);
