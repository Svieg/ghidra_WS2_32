# ghidra_WS2_32
Setting ordinals for WS2_32 in Ghidra for non-Windows machines.

Ghidra can't look up ordinals for WS2_32.dll on Linux since they don't have definitions and that DLL is not anywhere on the file system of the machine.

This script defines all ordinals and finds "WS2_32.DLL::Ordinal_*" functions and renames it to the appropriate name.