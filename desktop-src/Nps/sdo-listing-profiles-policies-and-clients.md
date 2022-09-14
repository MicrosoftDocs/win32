---
title: Listing Profiles, Policies, and Clients
description: Listing Profiles, Policies, and Clients
ms.assetid: 8bfbe4f6-b098-43c8-acb7-2c489ebe0ad3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Listing Profiles, Policies, and Clients

The following VBScript code enumerates the profiles, policies, and clients on the local computer.


```VB
Option Explicit

Const DATA_STORE_LOCAL = 0
Const PROPERTY_SDO_NAME = 2

Const PROPERTY_IAS_POLICIES_COLLECTION = 1025
Const PROPERTY_IAS_PROFILES_COLLECTION = 1026

Const PROPERTY_IAS_PROTOCOLS_COLLECTION = 1027

Const PROPERTY_RADIUS_CLIENTS_COLLECTION = 1029

Const PROPERTY_CLIENT_REQUIRE_SIGNATURE = 1024 
Const PROPERTY_CLIENT_SHARED_SECRET = 1026 
Const PROPERTY_CLIENT_NAS_MANUFACTURER = 1027 
Const PROPERTY_CLIENT_ADDRESS = 1028 


Const PROPERTY_PROFILE_ATTRIBUTES_COLLECTION = 1024
Const PROPERTY_ATTRIBUTE_ID = 1024
Const PROPERTY_ATTRIBUTE_DISPLAY_NAME = 1035

Const PROPERTY_POLICY_CONSTRAINT = 1024
Const PROPERTY_POLICY_MERIT = 1025 
Const PROPERTY_POLICY_PROFILE_NAME = 1028 
Const PROPERTY_POLICY_ACTION = 1029
Const PROPERTY_POLICY_CONDITIONS_COLLECTION = 1030

Const PROPERTY_CONDITION_TEXT = 1024


Dim sdoMachine, sdoServiceSDO
Dim sdoCollProfiles, sdoCollProtocols, sdoCollClients, sdoCollPolicies
Dim sdoCollAttributes, sdoCollConditions
Dim sdoRADIUS
Dim vtProfile, vtProtocol, vtClient, vtPolicy, vtAttribute, vtCondition

Set sdoMachine = CreateObject("IAS.SdoMachine")
sdoMachine.Attach vbNullString
Set sdoServiceSDO = sdoMachine.GetServiceSDO(DATA_STORE_LOCAL, "IAS")

'
' List Profiles and Attributes
'
Set sdoCollProfiles = sdoServiceSDO.GetProperty(PROPERTY_IAS_PROFILES_COLLECTION)

WScript.Echo sdoCollProfiles.Count & " Profiles found."
For Each vtProfile in sdoCollProfiles
    WScript.Echo "- " & Chr(34) & vtProfile.GetProperty(PROPERTY_SDO_NAME) & Chr(34)
    set sdoCollAttributes = vtProfile.GetProperty(PROPERTY_PROFILE_ATTRIBUTES_COLLECTION)
    WScript.Echo sdoCollAttributes.Count & " Attributes found."
    For Each vtAttribute in sdoCollAttributes
        WScript.Echo " - " & Chr(34) & vtAttribute.GetProperty(PROPERTY_SDO_NAME) & Chr(34)
        WScript.Echo "   LDAPName " & Chr(34) & vtAttribute.GetProperty(PROPERTY_ATTRIBUTE_DISPLAY_NAME) & Chr(34)
        WScript.Echo "   Id " & Chr(34) & vtAttribute.GetProperty(PROPERTY_ATTRIBUTE_ID) & Chr(34)
    Next 'vtAttribute
Next 'vtProfile

'
' List Policies and Conditions
'
Set sdoCollPolicies = sdoServiceSDO.GetProperty(PROPERTY_IAS_POLICIES_COLLECTION)

WScript.Echo sdoCollPolicies.Count & " Policies found."
For Each vtPolicy in sdoCollPolicies
    WScript.Echo "- " & Chr(34) & vtPolicy.GetProperty(PROPERTY_SDO_NAME) & Chr(34)

    WScript.Echo "  Merit " & Chr(34) & vtPolicy.GetProperty(PROPERTY_POLICY_MERIT) & Chr(34)
    WScript.Echo "  Policy Name " & Chr(34) & vtPolicy.GetProperty(PROPERTY_POLICY_PROFILE_NAME) & Chr(34)

    set sdoCollConditions = vtPolicy.GetProperty(PROPERTY_POLICY_CONDITIONS_COLLECTION)
    WScript.Echo sdoCollConditions.Count & " Conditions found."
    For Each vtCondition in sdoCollConditions
        WScript.Echo " - " & Chr(34) & vtCondition.GetProperty(PROPERTY_SDO_NAME) & Chr(34)
        WScript.Echo "   Text " & Chr(34) & vtCondition.GetProperty(PROPERTY_CONDITION_TEXT) & Chr(34)
    Next 'vtCondition
Next 'vtPolicy 

'
' List Clients
'
Set sdoCollProtocols = sdoServiceSDO.GetProperty(PROPERTY_IAS_PROTOCOLS_COLLECTION)
Set sdoRADIUS = sdoCollProtocols.Item("Microsoft Radius Protocol")
Set sdoCollClients = sdoRADIUS.GetProperty(PROPERTY_RADIUS_CLIENTS_COLLECTION)

WScript.Echo 
WScript.Echo sdoCollClients.Count & " Clients found."
For Each vtClient in sdoCollClients
    WScript.Echo "- " & Chr(34) & vtClient.GetProperty(PROPERTY_SDO_NAME) & Chr(34)
    WScript.Echo " - Require Signature " & Chr(34) & vtClient.GetProperty(PROPERTY_CLIENT_REQUIRE_SIGNATURE) & Chr(34)
    WScript.Echo " - Shared Secret " & Chr(34) & vtClient.GetProperty(PROPERTY_CLIENT_SHARED_SECRET) & Chr(34)
    WScript.Echo " - NAS Manufacturer" & Chr(34) & vtClient.GetProperty(PROPERTY_CLIENT_NAS_MANUFACTURER) & Chr(34)
    WScript.Echo " - Address" & Chr(34) & vtClient.GetProperty(PROPERTY_CLIENT_ADDRESS) & Chr(34)
Next 'vtClient
```



## Related topics

<dl> <dt>

[**CLIENTPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-clientproperties)
</dt> <dt>

[Enumerating Objects in a Collection](/windows/desktop/Nps/sdo-enumerating-objects-in-a-collection)
</dt> <dt>

[**IASCOMMONPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iascommonproperties)
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> <dt>

[**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo)
</dt> <dt>

[**ISdoMachine**](/windows/desktop/api/sdoias/nn-sdoias-isdomachine)
</dt> <dt>

[**RADIUSPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-radiusproperties)
</dt> </dl>

 

 