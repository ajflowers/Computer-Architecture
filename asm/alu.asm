; Sprint Challenge stretch goal:
; Add the ALU operations: `AND` `OR` `XOR` `NOT` `SHL` `SHR` `MOD`
;
; Expected output:
; 16
; 31
; 12




LDI R0,19
LDI R1,28
AND R0, R1
PRN R0      ;print 19 & 28
LDI R0,19
LDI R1,28
OR R0, R1
PRN R0      ;print 19 | 18
LDI R1,19
XOR R1,R0
PRN R1      ;print 19 ^ 31
HLT