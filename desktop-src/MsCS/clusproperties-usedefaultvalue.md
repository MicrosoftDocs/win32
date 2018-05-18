---
title: ClusProperties.UseDefaultValue method
description: Used in conjunction with ClusProperties.SaveChanges to return a property to its default value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6ac19293-d489-41ee-b585-6997a29591af'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["UseDefaultValue method Failover Cluster", "UseDefaultValue method Failover Cluster , ClusProperties collection", "ClusProperties collection Failover Cluster , UseDefaultValue method"]
topic_type:
- apiref
api_name:
- ClusProperties.UseDefaultValue
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperties.UseDefaultValue method

\[The **UseDefaultValue** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Used in conjunction with [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) to return a property to its default value.

## Syntax


```VB
ClusProperties.UseDefaultValue( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** specifying a property by name or by numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

**UseDefaultValue** works in conjunction with [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) as follows.

-   **UseDefaultValue** sets the value of the property in the collection to empty and flags the property as "use default."
-   When the [**SaveChanges**](clusproperties-savechanges.md) method is invoked, any property in the collection flagged as "use default" is not written to the [cluster database](cluster-database.md). Instead, **SaveChanges** method clears the property value stored in the cluster database, causing the property to revert to its the hard-coded default value.
-   If [**SaveChanges**](clusproperties-savechanges.md) is successful, it automatically calls [**ClusProperties.Refresh**](clusproperties-refresh.md), which reads the default value from the cluster database into the collection.

The hard-coded default value of a property is defined by the [Cluster service](cluster-service.md) or by a [resource DLL](resource-dlls.md). The [Cluster Properties](cluster-properties.md) reference section documents each of the properties defined by the Cluster service, including their default values.

The [**ClusProperties.Refresh**](clusproperties-refresh.md) method clears the "use default" flag without affecting cluster database.

## Examples

The following example uses **UseDefaultValue** to set all of an object's properties to their default values.


```VB
Option Explicit

Public Function RestoreDefaults(obj)
  Dim objProp
  Dim strOut

  For Each objProp in obj.CommonProperties
    objProp.UseDefaultValue
  Next
  objProp.CommonProperties.SaveChanges

  For Each objProp in obj.PrivateProperties
    objProp.UseDefaultValue
  Next
  objProp.PrivateProperties.SaveChanges

  For Each objProp in objProp.CommonProperties
    strOut = strOut & objProp.Name & " = " & CStr(objProp.Value) & _
             vbCrLf
  Next

  For Each objProp in objProp.CommonProperties
    strOut = strOut & objProp.Name & " = " & CStr(objProp.Value) & _
              vbCrLf
  Next

  WScript.Echo strOut

  Set objProp = Nothing

End Function
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





