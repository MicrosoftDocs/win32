---
title: Creating a Connection Request Policy
description: Creating a Connection Request Policy
ms.assetid: 659e7d1e-d985-4cb1-95ad-355c5b44d55a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Connection Request Policy

The following Visual Basic code creates a connection request policy. It adds a condition to the policy that matches on the name of the user requesting access. It links the policy to a profile. It configures that profile to use RADIUS for both authentication and accounting, and specifies the server groups that the profile should use for authentication and accounting.

> [!Note]  
> This in-line code sample has been built on managed Visual Basic.

 


```VB
   Copyright (c) Microsoft Corporation. All rights reserved. 
   
   Module Module1

   '//***************************************************************
   '//
   '// PUBLIC Sub Main
   '//
   '//***************************************************************
   Public Sub Main()

      '//************************************************************
      '//
      '// The following strings are defined here so that they can be easily
      '//  changed without searching through the code.
      '//
      '// The sample code here assumes that a server group named 
      '// "RADIUS Server Group Name" already exists.
      '//
      '//************************************************************
      Dim sNewCRPolicyName As String = "My Connection Request Policy"
      Dim sNewCRConditionName As String = "Condition1"
      Dim sCRConditionText As String = "MATCH(""User-Name=.*@microsoft.com"")"
      Dim sRADIUSServerGroupName As String = "RADIUS Server Group Name"

      '//************************************************************
      '//
      '// This section performs standard operations:
      '//  1) Create an sdoMachine object.
      '//  2) Attach the sdoMachine to the local machine.
      '//  3) Create the sdoDictionary object, which is needed later
      '//      to create attributes for the connection request profile.
      '//  4) Get the ISdo interface to the sdoService object for the "IAS"
      '//      service.
      '//  5) Get the ISdoServiceControl interface from the sdoService object. 
      '//
      '//************************************************************
      Dim sdoMachine As New SDOIASLib.SdoMachine()
      sdoMachine.Attach(vbNullString)

      Dim sdoDictionary As SDOIASLib.ISdoDictionaryOld = sdoMachine.GetDictionarySDO()
      Dim sdoServiceSDO As SDOIASLib.ISdo = sdoMachine.GetServiceSDO(SDOIASLib.IASDATASTORE.DATA_STORE_LOCAL, "IAS")
      Dim sdoServiceControl As SDOIASLib.ISdoServiceControl = sdoServiceSDO

      '//************************************************************
      '//
      '// The Connection Request Policies collection and Connection Request
      '//  Profiles collection are accessed directly from the sdoService
      '//  object.
      '//
      '//************************************************************
      '//************************************************************
      '//
      '// Please note: There is no requirement that a profile name be the
      '//  same as its associated policy name.  The profile file is linked
      '//  to the policy as a result of the value of a property belonging to the policy.
      '//
      '// The Windows IAS user interface components always associate
      '//  exactly one profile to exactly one policy and the profile is
      '//  named identically to the policy.  This is just the convention
      '//  of the administrative user interface.
      '//
      '// There is nothing to stop the user from setting up other naming
      '//  methods and associations, but if the naming convention deviates
      '//  from the stated convention, you will not be able to use the user interface to
      '//  make changes.
      '//
      '//************************************************************

      Dim colCRPolicies As SDOIASLib.ISdoCollection = sdoServiceSDO.GetProperty(SDOIASLib.IASPROPERTIES.PROPERTY_IAS_PROXYPOLICIES_COLLECTION)
      Dim colCRProfiles As SDOIASLib.ISdoCollection = sdoServiceSDO.GetProperty(SDOIASLib.IASPROPERTIES.PROPERTY_IAS_PROXYPROFILES_COLLECTION)

      '//************************************************************
      '//
      '// The policy or profile name must be unique within the collection,
      '//  so first check if the chosen policy name already exists.
      '//
      '// NOTES:
      '//      1) In a true solution, we would probably do one of three
      '//         things:
      '//          a) Allow the selection of a unique name.
      '//          b) Edit the existing policy/profile.
      '//          c) Delete the existing policy/profile.
      '//
      '//         Here, we simply exit if a policy with the same name
      '//          already exists.
      '//
      '//      2) This code assumes that the name of the profile is
      '//          identical to the name of the policy.  Further, it is
      '//          assumed that both elements of a policy/profile pair will
      '//          either exist or not exist.  There are situations when this
      '//          may not be true, so ideally the uniqueness of the name
      '//          should be checked against the profile collection as well.
      '//
      '//*************************************************************
      Dim sdoNewCRPolicy As SDOIASLib.ISdo, sdoNewCRProfile As SDOIASLib.ISdo
      If (colCRPolicies.IsNameUnique(sNewCRPolicyName) And _
          colCRProfiles.IsNameUnique(sNewCRPolicyName)) Then
         Call colCRPolicies.Add(sNewCRPolicyName, sdoNewCRPolicy)
         Call colCRProfiles.Add(sNewCRPolicyName, sdoNewCRProfile)

         Dim vtTemp As System.Object

         With sdoNewCRProfile
            Dim colCRAttributes As SDOIASLib.ISdoCollection = .GetProperty(SDOIASLib.PROFILEPROPERTIES.PROPERTY_PROFILE_ATTRIBUTES_COLLECTION)

            '//********************************************************
            '//
            '// Everything that must be set up in a connection request profile
            '//  is done using the Attributes collection.
            '//
            '// First, get the collection of attributes, then add the necessary
            '//  elements.
            '//
            '// The Attributes collection does not function like other
            '//  sdoCollection elements.  In order to add a new attribute to the
            '//  collection, you must first create a fully populated
            '//  stand-alone attribute element using the ISdoDictionaryOld
            '//  interface, then add that attribute object to the collection.
            '//  Therefore, it is not possible to add an attribute that is not
            '//  defined in the IAS dictionary.
            '//
            '//  The SDO methods expect data to be provided in exacting formats--
            '//  that is why a great deal of trouble is made to create VARIANT
            '//  values of just the right data type.
            '//
            '// NOTE: The SDOs perform no validation of data.  For example, any name
            '//       can be used in the code below for the RADIUS server group
            '//       name and the property set operation will succeed.  If the
            '//       set group does not exist, IAS logs a failure event and
            '//       the user interface can inform the user of the problem the next time
            '//       any sort of editing or viewing is done.  There is nothing to
            '//       stop you from using any particular name.
            '//
            '//******************************************************

            '//******************************************************
            '//
            '//      Attribute Name: Authentication Provider Type
            '//        Attribute ID: 4133
            '// Attribute Data Type: VT_I4 (Enumerated Value)
            '//
            '// Enumerated values for the "authentication provider type" attribute.
            '// IAS_AUTH_PROVIDER_RADIUS_PROXY = 2
            '//******************************************************
            Const IAS_AUTH_PROVIDER_RADIUS_PROXY As Long = 2

            Dim sdoNewCRAttribute As SDOIASLib.ISdo
            sdoNewCRAttribute = sdoDictionary.CreateAttribute(SDOIASLib.ATTRIBUTEID.IAS_ATTRIBUTE_AUTH_PROVIDER_TYPE)

            Dim sTemp As String

            With sdoNewCRAttribute
               sTemp = .GetProperty(SDOIASLib.IASCOMMONPROPERTIES.PROPERTY_SDO_NAME)
               Call colCRAttributes.Add(sTemp, sdoNewCRAttribute)
               vtTemp = CInt(IAS_AUTH_PROVIDER_RADIUS_PROXY)
               Call .PutProperty(SDOIASLib.ATTRIBUTEPROPERTIES.PROPERTY_ATTRIBUTE_VALUE, vtTemp)
               Call .Apply()
            End With 'sdoNewCRAttribte

            '//******************************************************
            '//
            '//      Attribute Name: Authentication Provider Name
            '//        Attribute ID: 4137
            '// Attribute Data Type: VT_BSTR
            '//
            '//*******************************************************
            sdoNewCRAttribute = sdoDictionary.CreateAttribute(SDOIASLib.ATTRIBUTEID.IAS_ATTRIBUTE_AUTH_PROVIDER_NAME)
            With sdoNewCRAttribute
               sTemp = .GetProperty(SDOIASLib.IASCOMMONPROPERTIES.PROPERTY_SDO_NAME)
               Call colCRAttributes.Add(sTemp, sdoNewCRAttribute)
               vtTemp = CStr(sRADIUSServerGroupName)
               Call .PutProperty(SDOIASLib.ATTRIBUTEPROPERTIES.PROPERTY_ATTRIBUTE_VALUE, vtTemp)
               Call .Apply()
            End With 'sdoNewCRAttribte

            '//******************************************************
            '//
            '//      Attribute Name: Accounting Provider Type
            '//        Attribute ID: 4138
            '// Attribute Data Type: VT_I4 (Enumerated Value)
            '//
            '// Enumerated values for the "accounting provider type" attribute.
            '// IAS_ACCT_PROVIDER_RADIUS_PROXY = 2
            '//******************************************************
            Const IAS_ACCT_PROVIDER_RADIUS_PROXY As Long = 2

            sdoNewCRAttribute = sdoDictionary.CreateAttribute(SDOIASLib.ATTRIBUTEID.IAS_ATTRIBUTE_ACCT_PROVIDER_TYPE)
            With sdoNewCRAttribute
               sTemp = .GetProperty(SDOIASLib.IASCOMMONPROPERTIES.PROPERTY_SDO_NAME)
               Call colCRAttributes.Add(sTemp, sdoNewCRAttribute)
               vtTemp = CInt(IAS_ACCT_PROVIDER_RADIUS_PROXY)
               Call .PutProperty(SDOIASLib.ATTRIBUTEPROPERTIES.PROPERTY_ATTRIBUTE_VALUE, vtTemp)
               Call .Apply()
            End With 'sdoNewCRAttribte

            '//*******************************************************
            '//
            '//      Attribute Name: Authentication Provider Name
            '//        Attribute ID: 4139
            '// Attribute Data Type: VT_BSTR
            '//
            '//*******************************************************
            sdoNewCRAttribute = sdoDictionary.CreateAttribute(SDOIASLib.ATTRIBUTEID.IAS_ATTRIBUTE_ACCT_PROVIDER_NAME)
            With sdoNewCRAttribute
               sTemp = .GetProperty(SDOIASLib.IASCOMMONPROPERTIES.PROPERTY_SDO_NAME)
               Call colCRAttributes.Add(sTemp, sdoNewCRAttribute)
               vtTemp = CStr(sRADIUSServerGroupName)
               Call .PutProperty(SDOIASLib.ATTRIBUTEPROPERTIES.PROPERTY_ATTRIBUTE_VALUE, vtTemp)
               Call .Apply()
            End With 'sdoNewCRAttribte

            '// Finally apply changes to the new Profile object.
            Call .Apply()
         End With 'sdoNewCRProfile

         '//**********************************************************
         '//
         '// The way this code is written can cause problems.  Because the
         '//  Profile object has been applied (above), the new object and its
         '//  associated data has been persisted through to the data store.
         '//  If the addition of the policy fails for any reason, the profile
         '//  must be backed out to keep extra garbage from collecting in the MDB.
         '//
         '//**********************************************************

         '//**********************************************************
         '//
         '// Important elements of a Policy object are:
         '//   1) Conditions
         '//   2) Associated profile name
         '//   3) Merit value
         '//
         '//**********************************************************

         With sdoNewCRPolicy

            '//*******************************************************
            '//
            '// A Condition object is a simple object with a name and a
            '//  PROPERTY_CONDITION_TEXT element.  The name of the object is not
            '//  significant, but it must be unique within the collection of
            '//  conditions.
            '//
            '// The condition itself is specified by a BSTR that contains the text of
            '//  the condition.
            '//
            '//********************************************************
            Dim colCRConditions As SDOIASLib.ISdoCollection = .GetProperty(SDOIASLib.POLICYPROPERTIES.PROPERTY_POLICY_CONDITIONS_COLLECTION)
            Dim sdoNewCRCondition As SDOIASLib.ISdo
            Call colCRConditions.Add(sNewCRConditionName, sdoNewCRCondition)
            With sdoNewCRCondition
               vtTemp = CStr(sCRConditionText)
               Call .PutProperty(SDOIASLib.CONDITIONPROPERTIES.PROPERTY_CONDITION_TEXT, vtTemp)
               .Apply()
            End With 'sdoNewCRCondition

            '//********************************************************
            '//
            '// The merit of the policy is the order in which it is evaluated
            '//  relative to other existing policies.
            '//
            '// NOTE: When a new policy is created, it does not matter what value
            '//       is placed in this property -- the new policy will always be
            '//       initially added with a merit of 1.  To change the ordering, the
            '//       merit value must be edited after the policy has been applied.
            '//
            '//********************************************************
            vtTemp = CInt(1)
            '            vtTemp = CLng(1)
            Call .PutProperty(SDOIASLib.POLICYPROPERTIES.PROPERTY_POLICY_MERIT, vtTemp)

            '//*******************************************************
            '//
            '// The policy name links it to an associated profile.
            '//
            '//*******************************************************
            vtTemp = CStr(sNewCRPolicyName)
            Call .PutProperty(SDOIASLib.POLICYPROPERTIES.PROPERTY_POLICY_PROFILE_NAME, vtTemp)

            Call .Apply()
         End With 'sdoNewCRPolicy

         '//**********************************************************
         '//
         '// Now the service needs to be refreshed to use the new configuration.
         '//
         '//**********************************************************

         Try
            Call sdoServiceControl.ResetService()
         Catch ex As Exception
            '//*******************************************************
            '//
            '//  IAS is likely not running. Ignore the exception.
            '//
            '//*******************************************************
         End Try

      End If 'IsNameUnique(sNewCRPolicyName)

   End Sub 'MAIN

End Module

```



## Related topics

<dl> <dt>

[Order in Which to Use the SDO API](/windows/desktop/Nps/sdo-order-in-which-to-use-the-sdo-api)
</dt> <dt>

[SDO Supported Attributes](/windows/desktop/Nps/sdo-sdo-supported-attributes)
</dt> <dt>

[**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo)
</dt> <dt>

[**ISdoCollection**](/windows/desktop/api/sdoias/nn-sdoias-isdocollection)
</dt> <dt>

[**ISdoDictionaryOld**](/windows/desktop/api/sdoias/nn-sdoias-isdodictionaryold)
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> <dt>

[**POLICYPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-policyproperties)
</dt> <dt>

[**PROFILEPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-profileproperties)
</dt> </dl>

 

 