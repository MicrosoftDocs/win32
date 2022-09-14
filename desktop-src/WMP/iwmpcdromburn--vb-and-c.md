---
title: IWMPCdromBurn (VB and C ) interface (Wmp.h)
description: Provides properties and methods to manage creating audio CDs.
ms.assetid: d98b243d-d6c2-4d85-8d5a-de49c62d0acf
keywords:
- IWMPCdromBurn (VB and C ) interface Windows Media Player
- IWMPCdromBurn (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPCdromBurn (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn (VB and C#) interface

Provides properties and methods to manage creating audio CDs.

## Members

The **IWMPCdromBurn (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPCdromBurn (VB and C#)** interface has these methods.



| Method                                                                             | Description                                                              |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**erase**](wmplibiwmpcdromburn-iwmpcdromburn-erase--vb-and-c.md)                 | Erases the current CD.<br/>                                        |
| [**getItemInfo**](wmplibiwmpcdromburn-iwmpcdromburn-getiteminfo-iwmpcdromburn.md) | Retrieves the value of the specified attribute for the CD.<br/>    |
| [**isAvailable**](wmplibiwmpcdromburn-iwmpcdromburn-isavailable--vb-and-c.md)     | Provides information about the CD drive and media.<br/>            |
| [**refreshStatus**](wmplibiwmpcdromburn-iwmpcdromburn-refreshstatus--vb-and-c.md) | Updates the status information for the current burn playlist.<br/> |
| [**startBurn**](wmplibiwmpcdromburn-iwmpcdromburn-startburn--vb-and-c.md)         | Burns the CD.<br/>                                                 |
| [**stopBurn**](wmplibiwmpcdromburn-iwmpcdromburn-stopburn-iwmpcdromburn.md)       | Stops the CD burning process.<br/>                                 |



 

### Properties

The **IWMPCdromBurn (VB and C#)** interface has these properties.



| Property                                                                                    | Access type          | Description                                                                 |
|:--------------------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**burnFormat**](wmplibiwmpcdromburn-iwmpcdromburn-burnformat--vb-and-c.md)<br/>     | Read-only<br/> | Gets a value that indicates the type of CD to burn.<br/>              |
| [**burnPlaylist**](wmplibiwmpcdromburn-iwmpcdromburn-burnplaylist--vb-and-c.md)<br/> | Read-only<br/> | Gets the current playlist to burn to the CD.<br/>                     |
| [**burnProgress**](wmplibiwmpcdromburn-iwmpcdromburn-burnprogress--vb-and-c.md)<br/> | Read-only<br/> | Gets the CD burning progress as percent complete.<br/>                |
| [**burnState**](wmplibiwmpcdromburn-iwmpcdromburn-burnstate--vb-and-c.md)<br/>       | Read-only<br/> | Gets an enumeration value that indicates the current burn state.<br/> |
| [**label**](wmplibiwmpcdromburn-iwmpcdromburn-label--vb-and-c.md)<br/>               | Read-only<br/> | Gets the CD volume label string.<br/>                                 |



 

Get an **IWMPCdromBurn** interface by casting the **IWMPCdrom** interface of the CD that you wish to burn.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 





