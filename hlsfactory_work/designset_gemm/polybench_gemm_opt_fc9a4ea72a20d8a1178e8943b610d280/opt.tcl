set_directive_resource -core RAM_1P "gemm" A
set_directive_resource -core RAM_1P "gemm" B
set_directive_resource -core RAM_1P "gemm" C
set_directive_interface -mode ap_fifo "gemm" D_out


set_directive_unroll -factor 2 gemm/lp3

set_directive_unroll -factor 8 gemm/lp5

