---
title: Offline compiling
description: The effect-compiler tool (fxc.exe) is designed for offline compilation of HLSL shaders.
ms.assetid: 56806335-a0c7-4247-b40d-ba93486a88ac
keywords:
- fxc, offline compiling
ms.topic: article
ms.date: 05/31/2018
---

# Offline compiling

The effect-compiler tool (fxc.exe) is designed for offline compilation of HLSL shaders.

## Compiling with the current compiler

The shader models supported by the current compiler are shown in [Profiles](dx-graphics-tools-fxc-syntax.md). This example compiles a pixel shader for the shader model 5.1 target.

```
fxc /T ps_5_1 /Fo PixelShader1.fxc PixelShader1.hlsl
```

In this example:

-   ps\_5\_1 is the target profile.
-   PixelShader1.fxc is the output object file containing the compiled shader.
-   PixelShader1.hlsl is the source.

```
fxc /Od /Zi /T ps_5_1 /Fo PixelShader1.fxc PixelShader1.hlsl
```

The debug options include additional options to disable compiler optimizations (Od) and enable debug information (Zi) like line numbers and symbols.

For a full listing of the command-line options, see the [Syntax](dx-graphics-tools-fxc-syntax.md) page.

## Compiling with the legacy compiler

Beginning with Direct3D 10, some shader models are no longer supported. These include pixel shader models: ps\_1\_1, ps\_1\_2, ps\_1\_3, and ps\_1\_4 which support very limited resources and are dependent on hardware. The compiler has been redesigned with shader model 2 (or greater) which allows for greater efficiencies with compilation. This of course will require that you are running on hardware that supports shader models 2 and greater.

Also note that you should consult the SDK release notes associated with your version of the FXC compiler for behavior affected by the /Gec switch.

## Using the effect-compiler tool in a subprocess

If fxc.exe is spawned as a subprocess by an application it is important to ensure that the application checks for and reads any data in output or error pipes passed to the CreateProcess function. If the application only waits for the subprocess to finish and one of the pipes becomes full the subprocess will never finish.

The following example code illustrates waiting on a subprocess and reading the output and error pipes attached to the subprocess. The contents of the `WaitHandles` array correspond to handles for the subprocess, the pipe for stdout and the pipe for stderr.

```cpp
HANDLE WaitHandles[] = {
  piProcInfo.hProcess, hReadOutPipe, hReadErrorPipe
};

const DWORD BUFSIZE = 4096;
BYTE buff[BUFSIZE];

while (1)
{
    DWORD dwBytesRead, dwBytesAvailable;

    dwWaitResult = WaitForMultipleObjects(3, WaitHandles, FALSE, 60000L);

    // Read from the pipes...
    while (PeekNamedPipe(hReadOutPipe, NULL, 0, NULL, &dwBytesAvailable, NULL) && dwBytesAvailable)
    {
        ReadFile(hReadOutPipe, buff, BUFSIZE - 1, &dwBytesRead, 0);
        streamOut << std::string((char*)buff, (size_t)dwBytesRead);
    }
    while (PeekNamedPipe(hReadErrorPipe, NULL, 0, NULL, &dwBytesAvailable, NULL) && dwBytesAvailable)
    {
        ReadFile(hReadErrorPipe, buff, BUFSIZE - 1, &dwBytesRead, 0);
        streamError << std::string((char*)buff, (size_t)dwBytesRead);
    }

    // Process is done, or we timed out:
    if (dwWaitResult == WAIT_OBJECT_0 || dwWaitResult == WAIT_TIMEOUT)
        break;
}
```

For additional information on spawning a process see the reference page for [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa).

## Related topics

* [Effect-Compiler Tool](fxc.md)