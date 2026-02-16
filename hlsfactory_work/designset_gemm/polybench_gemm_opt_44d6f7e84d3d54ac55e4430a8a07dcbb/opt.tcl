set_directive_resource -core RAM_1P "gemm" A
set_directive_resource -core RAM_1P "gemm" B
set_directive_resource -core RAM_1P "gemm" C
set_directive_interface -mode ap_fifo "gemm" D_out

set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" A
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" B
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" C
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" D_out
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" buff_A
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" buff_B
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" buff_C
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" buff_D_out
set_directive_array_partition -type cyclic -factor 8 -dim 2 "gemm" tmp1
set_directive_unroll -factor 8 "gemm/lprd_2"
set_directive_unroll -factor 8 "gemm/lpwr_2"


set_directive_pipeline "gemm/lprd_2"
set_directive_pipeline "gemm/lpwr_2"


set_directive_unroll -factor 4 gemm/lp3

set_directive_pipeline gemm/lp4
set_directive_unroll -factor 8 gemm/lp4

