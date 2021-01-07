---
description: Explains how to create a math input control.
ms.assetid: 59976b01-9032-4226-a160-e9b2d4b8b23b
title: Creating a Math Input Control
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Math Input Control

To create the math input control, you must:

-   [Include Headers and Libraries for the Math Input Control](#include-headers-and-libraries-for-the-math-input-control)
-   [Declare the Control Pointer and Call CoInitialize on the Control Pointer](#declare-the-control-pointer-and-call-coinitialize-on-the-control-pointer)
-   [Show the Control](#show-the-control)

## Include Headers and Libraries for the Math Input Control

The following code should be placed at the top of your code where you will be using the math input control.


```
   // includes for implementation
   #include "micaut.h"
   #include "micaut_i.c"
   
```



This code will add support for the math input control to your application.

## Declare the Control Pointer and Call CoInitialize on the Control Pointer

After you have included the headers for your control, you can declare the control pointer and can call CoInitialize on it to create a handle to the math input control interface. The following code can be placed in a class or as a global variable in your application's implementation:


```
   CComPtr<IMathInputControl> g_spMIC; // Math Input Control
   
```



The following code shows how you can call CoInitialize on the control pointer.


```
   HRESULT hr = CoInitialize(NULL);
   hr = g_spMIC.CoCreateInstance(CLSID_MathInputControl);
   
```



After calling CoInitialize on the control pointer, you have a reference to the control and can access the control's methods. For example, you could enable the extended set of controls as shown in the following example.


```
   hr = g_spMIC->EnableExtendedButtons(VARIANT_TRUE);
   
```



## Show the Control

The control will not automatically appear after you create it. To show the control, call the [**Show**](/windows/desktop/api/micaut/nf-micaut-imathinputcontrol-show) method on the control reference that you created in the previous step. The following code demonstrates how the [**Show**](/windows/win32/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_autoshow) method can be called.


```
   hr = g_spMIC->Show();
   
```



After the control shows, it will look something like the following illustration.

![screen shot showing math input control](images/mic.png)

Note that I have enabled the extended set of buttons so that **Redo** and **Undo** are available.

 

 
