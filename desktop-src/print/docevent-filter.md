---
Description: The DOCEVENT\_FILTER structure contains a list of document events to which the printer driver will respond. See DrvDocumentEvent for a complete list of the document events.
ms.assetid: f486efdb-79fd-4c57-bff6-75a0dbd68cc0
title: DOCEVENT\_FILTER structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DOCEVENT\_FILTER structure

The DOCEVENT\_FILTER structure contains a list of document events to which the printer driver will respond. See [**DrvDocumentEvent**](drvdocumentevent.md) for a complete list of the document events.

## Syntax


```C++
typedef struct _DOCEVENT_FILTER {
  UINT  cbSize;
  UINT  cElementsAllocated;
  UINT  cElementsNeeded;
  UINT  cElementsReturned;
  DWORD aDocEventCall[ANYSIZE_ARRAY];
} DOCEVENT_FILTER, *PDOCEVENT_FILTER;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Spooler-supplied size, in bytes, of this structure. The spooler initializes this member to **sizeof**(DOCEVENT\_FILTER).

</dd> <dt>

**cElementsAllocated**
</dt> <dd>

Spooler-supplied number of elements in the **aDocEventCall** array member. The spooler initializes this member to DOCUMENTEVENT\_LAST - 1. (The DOCUMENTEVENT\_LAST constant is defined in header file Winddiui.h.)

</dd> <dt>

**cElementsNeeded**
</dt> <dd>

Driver-supplied total number of elements needed in the **aDocEventCall** array member. The spooler initializes this member to 0XFFFFFFFF. For more information, see the following Remarks section.

</dd> <dt>

**cElementsReturned**
</dt> <dd>

Driver-supplied number of DOCUMENTEVENT\_*XXX* events that it placed in the **aDocEventCall** array member. The spooler initializes this member to 0XFFFFFFFF. For more information, see the following Remarks section.

</dd> <dt>

**aDocEventCall**
</dt> <dd>

Driver-filled array of DWORDs listing all of the DOCUMENTEVENT\_*XXX* events to which the printer driver will respond. The spooler initializes this member to 0.

</dd> </dl>

## Remarks

The DOCEVENT\_FILTER structure is defined for Windows XP and later.

The printer driver lists the events to which it will respond in the DOCEVENT\_FILTER structure. Because this limits the number of calls to the driver the spooler needs to make, printer performance is enhanced. When the spooler makes a call to the [**DrvDocumentEvent**](drvdocumentevent.md) DDI with its *iEsc* parameter set to DOCUMENTEVENT\_QUERYFILTER, the spooler allocates a buffer that contains a DOCEVENT\_FILTER structure, including its **aDocEventCall** array. The amount of memory allocated for the buffer is:


```
sizeof(DOCEVENT_FILTER) + sizeof(DWORD) * (DOCUMENTEVENT_LAST - 2)
 
```



After allocating a buffer that contains a DOCEVENT\_FILTER structure, the spooler initializes the structure members to the following values:



| Member                            | Initialized to:                                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------------------|
| **cbSize**<br/>             | 0<br/>                                                                                             |
| **cElementsAllocated**<br/> | DOCUMENTEVENT\_LAST - 1<br/> The DOCUMENTEVENT\_LAST constant is defined in winddiui.h.<br/> |
| **cElementsNeeded**<br/>    | 0XFFFFFFFF<br/>                                                                                    |
| **cElementsReturned**<br/>  | 0XFFFFFFFF<br/>                                                                                    |
| **aDocEventCall**<br/>      | 0<br/>                                                                                             |



 

After the spooler has initialized the structure members to the values shown in the preceding table, it then calls [**DrvDocumentEvent**](drvdocumentevent.md). When this function returns, the spooler inspects the **cElementsNeeded** and **cElementsReturned** members to see if either has been changed. If the driver has written to one of these members, but not the other, the spooler interprets the unwritten-to member as having the value 0.

If the driver supports DOCUMENTEVENT\_QUERYFILTER:

-   If the **aDocEventCall** array is large enough to contain all of the DOCUMENTEVENT\_*XXX* events the printer driver intends to place in it, the printer driver:
    -   Fills the array with those events.
    -   Sets the **cElementsReturned** member to that number of events (which should be less than or equal to **cElementsAllocated**).
    -   Leaves **cElementsNeeded** unchanged.
    -   Returns DOCUMENTEVENT\_SUCCESS.

<dl> In this case, the spooler uses the first **cElementsReturned** values in the **aDocEventCall** array.  
</dl>

> [!Note]  
> The DOCUMENTEVENT\_CREATEDCPRE event is treated in a special way. When the spooler calls [**DrvDocumentEvent**](drvdocumentevent.md) with the *iEsc* parameter set to DOCUMENTEVENT\_CREATEDCPRE, the spooler uses the return value to determine whether future calls to this function are necessary. Unlike other DOCUMENTEVENT\_*XXX* events, the printer driver always receives calls to **DrvDocumentEvent** with DOCUMENTEVENT\_CREATEDCPRE, whether this event is filtered out or not.

 

-   If the **aDocEventCall** array is not large enough to contain all of the DOCUMENTEVENT\_*XXX* events the printer driver intends to place in it, the printer driver should:

    -   Set **cElementsNeeded** to the number of events to which it intends to respond (which should be greater than **cElementsAllocated**).
    -   Leave **cElementsReturned** unchanged.
    -   Return DOCUMENTEVENT\_SUCCESS.

    In this case, the spooler then allocates a new buffer that is sufficiently large, and then makes another call to [**DrvDocumentEvent**](drvdocumentevent.md) with DOCUMENTEVENT\_QUERYFILTER.

If the driver does not support the DOCUMENTEVENT\_QUERYFILTER event, it should return DOCUMENTEVENT\_UNSUPPORTED. If the driver does support DOCUMENTEVENT\_QUERYFILTER, but encounters internal errors when it handles this event, it should return DOCUMENTEVENT\_FAILURE. In either case, the spooler is not able to retrieve the event filter from the driver, so it continues in its behavior of calling [**DrvDocumentEvent**](drvdocumentevent.md) for all events.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDocumentEvent**](drvdocumentevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOCEVENT_FILTER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





