vars: r0 r1 r2 r3 r4 r5 r6 r7 r8 fibonacci
function fibonacci 1 0
arg r0 0 0
if_less_than_two r0 label_true label_false
label_true 0 0 0
minus r3 1 0
minus r4 2 0
call r5 fibonacci r3
call r6 fibonacci r4
plus r7 r5 r6
return r7 0 0
label_false 0 0 0
return 1 0 0
begin_program 0 0 0
readln r1 0 0
call r2 fibonacci r1
print r2 0 0
end_program 0 0 0
