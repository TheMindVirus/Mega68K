import capstone

def decipher(code, offset = 0, index = 0):
    result = ""
    disassembler = capstone.Cs(capstone.CS_ARCH_M68K, capstone.CS_MODE_BIG_ENDIAN)
    disassembly = disassembler.disasm(code, offset)
    for step in disassembly:
        hexd = "0x{}".format(step.bytes.hex().upper())
        bind = "0b{:016b}".format(int.from_bytes(step.bytes, "big"))
        line = "0x{:08x}: ({} | {}) {} : {} {}".format(step.address + index, hexd, bind, step.size, step.mnemonic, step.op_str)
        result += str(line) # + "\n"
    return result

def extract(binstr):
    binstr = binstr.replace("-", "0").replace(" ", "").replace(",", "")
    hi = int(binstr[0:8], 2)
    lo = int(binstr[8:16], 2)
    return bytearray((hi, lo))

def printout():
    for i in range(0, pow(2, 16)):
        line = decipher(i.to_bytes(2, "big"), i)
        print(line)

def search(term = "", first = True):
    for i in range(0, pow(2, 16)):
        line = decipher(i.to_bytes(2, "big"), i)
        if term in line:
            print(line)
            if first:
                break
opcodes = \
[
    # [Motorola-68010-Reference-Platform] 
    # D15 -> D0
    extract("1100---1 --------"), #ABCD
    extract("1101---- --------"), #ADD
    extract("1101---- 11------"), #ADDA
    extract("1101---- --------"), #ADDQ
    extract("0000-11- --------"), #ADDI
    extract("1101---1 --------"), #ADDX
    extract("1100---- --------"), #AND
    extract("0000--1- --------"), #ANDI
    extract("1110---1 --------"), #ASL    
    extract("1110---- --------"), #ASR

    extract("0110-10- --------"), #BCC
    extract("0000---1 -1------"), #BCHG
    extract("0000---1 1-------"), #BCLR
    extract("0110---- --------"), #BRA
    extract("0000---1 11------"), #BSET
    extract("0110---1 --------"), #BSR
    extract("0000---1 --------"), #BTST

    extract("0100---1 1-------"), #CHK
    extract("0100--1- --------"), #CLR
    extract("1011---- --------"), #CMP
    extract("1011---- 11------"), #CMPA
    extract("1011---1 ----1---"), #CMPM
    extract("000011-- --------"), #CMPI

    extract("0101-1-- 11--1---"), #DBCC
    extract("1000---1 11------"), #DIVS
    extract("1000---- 11------"), #DIVU

    extract("1011---1 --------"), #EOR
    extract("00001-1- --------"), #EORI
    extract("1100---1 -1------"), #EXG
    extract("01001--- 1-------"), #EXT

    extract("0100111- 11-1----"), #JMP
    extract("0100111- 1--1----"), #JSR

    extract("0100---1 11-1----"), #LEA
    extract("0100111- -1-1----"), #LINK
    extract("1110---1 ----1---"), #LSL
    extract("1110---- ----1---"), #LSR

    extract("0001---- --------"), #MOVE
    extract("0010---- -1------"), #MOVEA
    extract("0100111- -1111-1-"), #MOVEC(DC)
    extract("01001--- 1--1----"), #MOVEM
    extract("0000---1 ----1---"), #MOVEP
    extract("0111---- --------"), #MOVEQ
    extract("0000111- --------"), #MOVES(???)
    extract("1100---1 11------"), #MULS
    extract("1100---- 11------"), #MULU

    extract("01001--- --------"), #NBCD
    extract("0100-1-- --------"), #NEG
    extract("0100---- --------"), #NEGX
    extract("0100111- -111---1"), #NOP
    extract("0100-11- --------"), #NOT

    extract("1000---- --------"), #OR
    extract("0000---- --------"), #ORI

    extract("01001--- -1-1----"), #PEA

    extract("0100111- -111----"), #RESET
    extract("1110---1 ---11---"), #ROL
    extract("1110---- ---11---"), #ROR
    extract("1110---1 ---1----"), #ROXL
    extract("1110---- ---1----"), #ROXR
    extract("0100111- -111-1--"), #RTD(DC)
    extract("0100111- -111--11"), #RTE
    extract("0100111- -111-111"), #RTR
    extract("0100111- -111-101"), #RTS

    extract("1000---1 --------"), #SBCD
    extract("0101-1-- 11------"), #SCC
    extract("0100111- -111--1-"), #STOP
    extract("1001---- --------"), #SUB
    extract("1001---- 11------"), #SUBA
    extract("0000-1-- --------"), #SUBI
    extract("0101---1 --------"), #SUBQ
    extract("1001---1 --------"), #SUBX
    extract("01001--- -1------"), #SWAP

    extract("01001-1- 11------"), #TAS
    extract("0100111- -1------"), #TRAP
    extract("0100111- -111-11-"), #TRAPV
    extract("01001-1- --------"), #TST

    extract("0100111- -1-11---"), #UNLK
]

if __name__ == "__main__":
    #printout()

    for opcode in opcodes:
        print(decipher(opcode))
    print()
    
    #search(" abcd.", False)
    #search(" unlk")

    #print("Done!")
