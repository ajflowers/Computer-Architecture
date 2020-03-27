; Sprint Challenge stretch goal:
; Add the ALU operations: `AND` `OR` `XOR` `NOT` `SHL` `SHR` `MOD`
;
; Expected output:
; 16
; 31

LDI R0,19
LDI R1,28
AND R0, R1
PRN R0
LDI R0,19
LDI R1,28
OR R0, R1
PRN R0
HLT