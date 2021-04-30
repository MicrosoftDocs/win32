---
description: Many of the debugging facilities described in this topic are implemented in the DirectShow base class library. For more information, see DirectShow Base Classes.
ms.assetid: 40b4f2ab-e629-41a0-b979-d74ac5fe83a2
title: Debugging DirectShow Filters
ms.topic: article
ms.date: 05/31/2018
---

# Debugging DirectShow Filters

Many of the debugging facilities described in this topic are implemented in the DirectShow base class library. For more information, see [DirectShow Base Classes](directshow-base-classes.md).

## Assertion Checking

Use assertion checking liberally. Assertions can verify assumptions that you make in your code about preconditions and postconditions. DirectShow provides several assertion macros. For more information, see [Assert and Breakpoint Macros](assert-and-breakpoint-macros.md).

## Object Names

In debug builds, there is a global list of objects that derive from the [**CBaseObject**](cbaseobject.md) class. As objects are created, they are added to the list. When they are destroyed, they are removed from the list. To display a list of those objects, call the [**DbgDumpObjectRegister**](dbgdumpobjectregister.md) function.

The constructor method for the [**CBaseObject**](cbaseobject.md) base class—and most classes derived from it—includes a parameter for the name of the object. Give your objects unique names to identify them. Use the [**NAME**](name.md) macro when you declare the name, so that the name is allocated only in debug builds. In retail builds, the name becomes **NULL**.

## Debug Logging

The [**DbgLog**](dbglog.md) function displays debugging messages as your program executes. Use this function to trace the execution of your application or filter. You can log return codes, the values of variables, and any other relevant information.

Every debug message has a type, such as LOG\_TRACE or LOG\_ERROR, and a debug level, which indicates the importance of the message. Messages with lower debug levels are more important than those with higher levels.

In the following example, a hypothetical filter disconnects a pin from an array of pins. If the disconnect attempt succeeds, the filter displays a LOG\_TRACE message. If the attempt fails, it displays a LOG\_ERROR message:


```C++
hr = m_PinArray[iPin]->Disconnect();
if (FAILED(hr))
{
    DbgLog((
        LOG_ERROR, 
        1, 
        TEXT("Could not disconnect pin %d. HRESULT = %#x", 
        iPin, 
        hr
        ));
 
   // Error handling code (not shown).
}
DbgLog((LOG_TRACE, 3, TEXT("Disconnected pin %d"), iPin));
```



When you are debugging, you can set the debug level for each message type. Also, each module (DLL or executable) maintains its own debugging levels. If you are testing a filter, raise the debug levels for the DLL that contains the filter.

For more information, see [Debug Output Functions](debug-output-functions.md).

## Critical Sections

To make deadlocks easier to track, include assertions that determine whether the calling code owns a given critical section. The [**CritCheckIn**](critcheckin.md) and [**CritCheckOut**](critcheckout.md) functions indicate whether the calling thread owns a critical section. Typically, you would call these functions from inside an assert macro.

You can also use the [**DbgLockTrace**](dbglocktrace.md) function to trace when critical sections are held or released.

## Related topics

<dl> <dt>

[Debugging in DirectShow](debugging-in-directshow.md)
</dt> </dl>

 

 



