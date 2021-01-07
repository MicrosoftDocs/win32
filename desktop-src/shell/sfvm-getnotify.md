---
description: Notification sent to the view callback object to specify the locations and events that should be registered for change notification events.
title: SFVM_GETNOTIFY message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 87933217-dfa9-4aaf-9630-fa2c302b18fa
api_name: 
 - SFVM_GETNOTIFY
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_GETNOTIFY message

Notification sent to the view callback object to specify the locations and events that should be registered for change notification events. Once they are registered, when a change occurs in on of these locations or events, the view callback object is notified. These events are sent to the view callback through [**SFVM\_FSNOTIFY**](sfvm-fsnotify.md) and are then handled by the view.


```C++
SFVM_GETNOTIFY 

    wParam = (WPARAM)(LPITEMIDLIST*) pidl;

    lParam = (LPARAM)(LONG*) lEvents;

            
```



## Parameters

<dl> <dt>

*pidl* \[out\]
</dt> <dd>

A pointer to an absolute IDList of an item for which the view should register to be notified of changes. Typically, this is the same as the IDList of the location being viewed, but it can be another location.

> [!IMPORTANT]
> The lifetime of this value is owned by the view callback object. It is the responsibility of the view callback object to create and then free this value when it is no longer needed. This requires that the view callback object stores this value. Usually, the value can be stored in the **\_pidlMonitor** member of the view callback object. The ownership rules for the value returned through *pidl* are nonstandard and require special care. The view callback object must own this value and ensure that it is not freed until the view callback object itself is destroyed.

 

</dd> <dt>

*lEvents* \[out\]
</dt> <dd>

A value that contains one or more SHCNE values. See [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify) for a list of possible values. The view callback object will register to receive an [**SFVM\_FSNOTIFY**](sfvm-fsnotify.md) message when any of the associated events occurs.

</dd> </dl>

## Return value

Ignored, but should return S\_OK.

## Remarks

If this callback message does not return a nonzero value for either the IDList or the events mask then the view will not register for change notifications.

## Examples

The following sample shows an example implementation of the view callback function's handler code for **SFVM\_GETNOTIFY**.


```C++
case SFVM_GETNOTIFY:
  *((LPITEMIDLIST*)wParam) = _pidl;    // Pass a reference whose lifetime this 
                                       // class is responsible for.
                                      
  *((LONG*)lParam) = SHCNE_DISKEVENTS; // A combination of all of the 
                                       // disk event identifiers.
                                       
   return S_OK;
```



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



## See also

<dl> <dt>

[**SFVM\_QUERYFSNOTIFY**](sfvm-queryfsnotify.md)
</dt> <dt>

[**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb)
</dt> </dl>

 

 
