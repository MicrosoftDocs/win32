---
title: sessionStateChangeType Simple Type
description: Defines values for the kind of Terminal Server session state change you can use to trigger a task to start.
ms.assetid: 56e19ec0-ea6c-4434-ab9d-a1069108920f
keywords:
- sessionStateChangeType simple type Task Scheduler
topic_type:
- apiref
api_name:
- sessionStateChangeType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# sessionStateChangeType Simple Type

Defines values for the kind of Terminal Server session state change you can use to trigger a task to start.

``` syntax
<xs:simpleType name="sessionStateChangeType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="ConsoleConnect"
         />
        <xs:enumeration
            value="ConsoleDisconnect"
         />
        <xs:enumeration
            value="RemoteConnect"
         />
        <xs:enumeration
            value="RemoteDisconnect"
         />
        <xs:enumeration
            value="SessionLock"
         />
        <xs:enumeration
            value="SessionUnlock"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **sessionStateChangeType** simple type defines the following values.



| Value             | Description                                                                                                                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ConsoleConnect    | Terminal Server console connection state change. For example, when you connect to a user session on the local computer by switching users on the computer. <br/>                            |
| ConsoleDisconnect | Terminal Server console disconnection state change. For example, when you disconnect to a user session on the local computer by switching users on the computer. <br/>                      |
| RemoteConnect     | Terminal Server remote connection state change. For example, when a user connects to a user session by using the Remote Desktop Connection program from a remote computer. <br/>            |
| RemoteDisconnect  | Terminal Server remote disconnection state change. For example, when a user disconnects from a user session while using the Remote Desktop Connection program from a remote computer. <br/> |
| SessionLock       | Terminal Server session locked state change. For example, this state change causes the task to run when the computer is locked. <br/>                                                       |
| SessionUnlock     | Terminal Server session unlocked state change. For example, this state change causes the task to run when the computer is unlocked.<br/>                                                    |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





