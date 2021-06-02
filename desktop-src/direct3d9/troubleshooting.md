---
description: This topic lists common categories of problems that you might encounter when writing Direct3D applications, and how to prevent them.
ms.assetid: 27b87f0f-7118-4252-b6e8-6ea18a9399e4
title: Troubleshooting (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting (Direct3D 9)

This topic lists common categories of problems that you might encounter when writing Direct3D applications, and how to prevent them.

## Device Creation

If your application fails during device creation, check for the following common errors.

-   Make sure you check the device capabilities, particularly the render depths.
-   Examine the error code. D3DERR\_OUTOFVIDEOMEMORY is always possible.
-   Use the debug DirectX dynamic-link libraries (DLLs) and review output messages under the debugger.

## Using Lit Vertices

Applications that use lit vertices should disable the Direct3D lighting engine by setting the D3DRS\_LIGHTING render state to **FALSE**. By default, when lighting is enabled, the system sets the color for any vertex that doesn't contain a normal vector to 0 (black), even if the input vertex contained a nonzero color value. Because lit-vertices don't, by their nature, contain a vertex normal, any color information passed to Direct3D is lost during rendering if the lighting engine is enabled.

Obviously, vertex color is important to any application that performs its own lighting. To prevent the system from imposing the default values, make sure you set D3DRS\_LIGHTING to **FALSE**.

If your application runs but nothing is visible, check for the following common errors.

-   Ensure that your triangles are not degenerate.
-   Ensure that your triangles are not being culled.
-   Make sure that your transformations are internally consistent.
-   Check the viewport settings to be sure they allow your triangles to be seen.

## Debugging

Debugging a Direct3D application can be challenging. Try the following techniques, in addition to checking all the return values - a particularly important piece of advice in Direct3D programming, which is dependent on very different hardware implementations.

-   Switch to debug DLLs.
-   Force a software-only device, turning off hardware acceleration even when it is available.
-   Force surfaces into system memory.
-   Create an option to run in a window, so that you can use an integrated debugger.

The second and third options in this list can help you avoid the Win16 lock which can otherwise cause your debugger to hang.

Also, try adding the following entries to Win.ini.


```
[Direct3D] 
debug=3 
[DirectDraw] 
debug=3 
```



## Borland Floating-Point Initialization

Compilers from Borland report floating-point exceptions in a manner that is incompatible with Direct3D. To solve this problem, include a \_matherr exception handler like the following:


```
// Borland floating point initialization 
#include <math.h>
#include <float.h>

void initfp(void)
{
    // Disable floating point exceptions
    _control87(MCW_EM,MCW_EM);
}

int _matherr(struct _exception  *e)
{
    e;               // Dummy reference to catch the warning
    return 1;        // Error has been handled
}
```



## Parameter Validation

For performance reasons, the debug version of the Direct3D Immediate Mode run time performs more parameter validation than the retail version, which sometimes performs no validation at all. This enables applications to perform robust debugging with the slower debug run-time component before using the faster retail version for performance tuning and final release.

Although several Direct3D Immediate Mode methods impose limits on the values that they can accept, these limits are often only checked and enforced by the debug version of the Direct3D Immediate Mode run time. Applications must conform to these limits, or unpredictable and undesirable results can occur when running on the retail version of Direct3D. For example, the [**IDirect3DDevice9::DrawPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawprimitive) method accepts a parameter (PrimitiveCount) that indicates the number of primitives that the method will render. The method can only accept values between 0 and D3DMAXNUMPRIMITIVES. In the debug version of Direct3D, if you pass more than D3DMAXNUMPRIMITIVES primitives, the method fails gracefully, printing an error message to the error log, and returning an error value to your application. Conversely, if your application makes the same error when it is running with the retail version of the run time, behavior is undefined. For performance reasons, the method does not validate the parameters, resulting in unpredictable and completely situational behavior when they are not valid. In some cases the call might work, and in other cases it might cause a memory fault in Direct3D. If an invalid call consistently works with a particular hardware configuration and DirectX version, there is no guarantee that it will continue to function on other hardware or with later releases of DirectX.

If your application encounters unexplained failures when running with the retail Direct3D run-time file, test against the debug version and look closely for cases where your application passes invalid parameters. Use the DirectX control panel applet, switch to the debug runtime if necessary, and check the "Break on D3DError" option. This option will force the runtime to use the Windows DebugBreak method in order to force the application to stop when an application bug is detected.

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
