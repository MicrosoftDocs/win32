---
description: The IAMTimelineObj interface provides methods for manipulating timeline objects in DirectShow Editing Services (DES).
ms.assetid: ae8a778d-00b3-4b88-98dd-16e0a8645127
title: IAMTimelineObj interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineObj` interface provides methods for manipulating timeline objects in [DirectShow Editing Services](directshow-editing-services.md) (DES). All timeline objects implement this method, including source, effect, transition, track, group, and composition objects. Create a timeline object by calling the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method.

## Members

The **IAMTimelineObj** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineObj** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineObj** interface has these methods.



| Method                                                          | Description                                                                                                                            |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearDirty**](iamtimelineobj-cleardirty.md)                 | Not supported.<br/>                                                                                                              |
| [**FixTimes**](iamtimelineobj-fixtimes.md)                     | Rounds the specified start and stop times to the nearest frame boundaries.<br/>                                                  |
| [**FixTimes2**](iamtimelineobj-fixtimes2.md)                   | Rounds the specified start and stop times, specified as [**REFTIME**](reftime.md) values, to the nearest frame boundaries.<br/> |
| [**GetDirtyRange**](iamtimelineobj-getdirtyrange.md)           | Not supported.<br/>                                                                                                              |
| [**GetDirtyRange2**](iamtimelineobj-getdirtyrange2.md)         | Not supported.<br/>                                                                                                              |
| [**GetEmbedDepth**](iamtimelineobj-getembeddepth.md)           | Not supported.<br/>                                                                                                              |
| [**GetGenID**](iamtimelineobj-getgenid.md)                     | Retrieves the object's generated identifier.<br/>                                                                                |
| [**GetGroupIBelongTo**](iamtimelineobj-getgroupibelongto.md)   | Not supported.<br/>                                                                                                              |
| [**GetLocked**](iamtimelineobj-getlocked.md)                   | Retrieves the object's editing state (locked or unlocked).<br/>                                                                  |
| [**GetMuted**](iamtimelineobj-getmuted.md)                     | Retrieves the object's muted state.<br/>                                                                                         |
| [**GetPropertySetter**](iamtimelineobj-getpropertysetter.md)   | Retrieves the object's property setter.<br/>                                                                                     |
| [**GetStartStop**](iamtimelineobj-getstartstop.md)             | Retrieves the object's start and stop times, relative to the object's parent.<br/>                                               |
| [**GetStartStop2**](iamtimelineobj-getstartstop2.md)           | Retrieves the object's start and stop times, as [**REFTIME**](reftime.md) values.<br/>                                          |
| [**GetSubObject**](iamtimelineobj-getsubobject.md)             | Retrieves the subobject associated with this object.<br/>                                                                        |
| [**GetSubObjectGUID**](iamtimelineobj-getsubobjectguid.md)     | Retrieves the GUID of the subobject associated with this timeline object.<br/>                                                   |
| [**GetSubObjectGUIDB**](iamtimelineobj-getsubobjectguidb.md)   | Retrieves the GUID of the subobject as a **BSTR** value.<br/>                                                                    |
| [**GetSubObjectLoaded**](iamtimelineobj-getsubobjectloaded.md) | Determines whether the object's subobject pointer has been set.<br/>                                                             |
| [**GetTimelineNoRef**](iamtimelineobj-gettimelinenoref.md)     | Not supported.<br/>                                                                                                              |
| [**GetTimelineType**](iamtimelineobj-gettimelinetype.md)       | Retrieves the object's type.<br/>                                                                                                |
| [**GetUserData**](iamtimelineobj-getuserdata.md)               | Retrieves the application-defined persistent data.<br/>                                                                          |
| [**GetUserID**](iamtimelineobj-getuserid.md)                   | Retrieves the object's application-defined identifier.<br/>                                                                      |
| [**GetUserName**](iamtimelineobj-getusername.md)               | Retrieves the object's application-defined name.<br/>                                                                            |
| [**Remove**](iamtimelineobj-remove.md)                         | Removes this object from the timeline, for reinsertion elsewhere.<br/>                                                           |
| [**RemoveAll**](iamtimelineobj-removeall.md)                   | Permanently removes this object from the timeline, including subobjects and children.<br/>                                       |
| [**SetDirtyRange**](iamtimelineobj-setdirtyrange.md)           | Not implemented.<br/>                                                                                                            |
| [**SetDirtyRange2**](iamtimelineobj-setdirtyrange2.md)         | Not implemented.<br/>                                                                                                            |
| [**SetLocked**](iamtimelineobj-setlocked.md)                   | Sets the object's editing state to locked or unlocked.<br/>                                                                      |
| [**SetMuted**](iamtimelineobj-setmuted.md)                     | Sets the object's muted state.<br/>                                                                                              |
| [**SetPropertySetter**](iamtimelineobj-setpropertysetter.md)   | Sets the object's property setter.<br/>                                                                                          |
| [**SetStartStop**](iamtimelineobj-setstartstop.md)             | Sets the object's start and stop times, relative to the timeline.<br/>                                                           |
| [**SetStartStop2**](iamtimelineobj-setstartstop2.md)           | Sets the object's start and stop times, as **REFTIME** values.<br/>                                                              |
| [**SetSubObject**](iamtimelineobj-setsubobject.md)             | Not supported.<br/>                                                                                                              |
| [**SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md)     | Specifies the globally unique identifier (GUID) of the subobject associated with this object.<br/>                               |
| [**SetSubObjectGUIDB**](iamtimelineobj-setsubobjectguidb.md)   | Specifies the GUID of the subobject as a **BSTR** value.<br/>                                                                    |
| [**SetTimelineType**](iamtimelineobj-settimelinetype.md)       | Not supported.<br/>                                                                                                              |
| [**SetUserData**](iamtimelineobj-setuserdata.md)               | Sets application-defined persistent data.<br/>                                                                                   |
| [**SetUserID**](iamtimelineobj-setuserid.md)                   | Sets an application-defined identifier for the object.<br/>                                                                      |
| [**SetUserName**](iamtimelineobj-setusername.md)               | Sets an application-defined name for the object.<br/>                                                                            |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 
