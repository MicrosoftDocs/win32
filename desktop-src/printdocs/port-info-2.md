---
description: The PORT\_INFO\_2 structure identifies a supported printer port.
ms.assetid: 93675294-61d4-40e4-b84c-f252978e0285
title: PORT_INFO_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PORT_INFO_2
- _PORT_INFO_2A
- _PORT_INFO_2W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PORT\_INFO\_2 structure

The **PORT\_INFO\_2** structure identifies a supported printer port.

## Syntax


```C++
typedef struct _PORT_INFO_2 {
  LPTSTR pPortName;
  LPTSTR pMonitorName;
  LPTSTR pDescription;
  DWORD  fPortType;
  DWORD  Reserved;
} PORT_INFO_2, *PPORT_INFO_2;
```



## Members

<dl> <dt>

**pPortName**
</dt> <dd>

Pointer to a null-terminated string that identifies a supported printer port (for example, "LPT1:").

</dd> <dt>

**pMonitorName**
</dt> <dd>

Pointer to a null-terminated string that identifies an installed monitor (for example, "PJL monitor"). This can be **NULL**.

</dd> <dt>

**pDescription**
</dt> <dd>

Pointer to a null-terminated string that describes the port in more detail (for example, if **pPortName** is "LPT1:", **pDescription** is "printer port"). This can be **NULL**.

</dd> <dt>

**fPortType**
</dt> <dd>

Bitmask describing the type of port. This member can be a combination of the following values:

<dl><span id="PORT_TYPE_WRITE"></span><span id="port_type_write"></span><dt>

**PORT\_TYPE\_WRITE**
</dt><span id="PORT_TYPE_READ"></span><span id="port_type_read"></span><dt>

**PORT\_TYPE\_READ**
</dt><span id="PORT_TYPE_REDIRECTED"></span><span id="port_type_redirected"></span><dt>

**PORT\_TYPE\_REDIRECTED**
</dt><span id="PORT_TYPE_NET_ATTACHED"></span><span id="port_type_net_attached"></span><dt>

**PORT\_TYPE\_NET\_ATTACHED**
</dt> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

Reserved; must be zero.

</dd> </dl>

## Remarks

Use the **PORT\_INFO\_2** structure when calling [**EnumPorts**](enumports.md) if there are multiple monitors installed that support the same ports.

The **fPortType** member can be queried to determine information about the port. Note that port settings do not influence printer attributes (as returned by the **Attributes** member of [**PRINTER\_INFO\_2**](printer-info-2.md)).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PORT\_INFO\_2W** (Unicode) and **\_PORT\_INFO\_2A** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> </dl>

 

 




