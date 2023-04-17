from bcc import BPF

BPF_PROGRAM = r"""
#include <uapi/linux/ptrace.h>

int kprobe__sys_execve(struct pt_regs *ctx) {
    char comm[16];
    bpf_get_current_comm(&comm, sizeof(comm));
    bpf_trace_printk("execve called by %s\n", comm);
    return 0;
}
"""

bpf = BPF(text=BPF_PROGRAM)

print("Tracing execve() calls... Ctrl-C to exit.")
bpf.trace_print()
