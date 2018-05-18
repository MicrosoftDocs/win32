---
title: How to Use document tracking
description: Using the document tracking feature requires some simple understandings about managing the associated metadata and registration with the service.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '70E10936-7953-49B0-B0DC-A5E7C4772E60'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["How to Use document tracking"]
topic_type:
- apiref
api_name:
- How to Use document tracking
api_type:
- NA
---

# How to: Use document tracking

Using the document tracking feature requires some simple understandings about managing the associated metadata and registration with the service.

## Managing document tracking metadata

Each of the operating systems supporting document tracking have similar implementations. These include as set of properties that represent the metadata, a new parameter added to the user policy creation methods and a method for registering the policy to be tracked with the document tracking service.

Operationally, only the **content name** and the **notification type** properties are required for document tracking.

The sequence of steps you will use to setup document tracking for a given piece of content is:

-   Create a **license metadata** object.

    See [**LicenseMetadata**](licensemetadata-interface-java.md) or [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) for more information.

-   Set the **content name** and **notification type**. These are the only required properties.

    For more information, see the property access methods for the platform appropriate license metadata class, either [**LicenseMetadata**](licensemetadata-interface-java.md) or [**MSLicenseMetadata**](mslicensemetadata-class-objc.md).

-   By policy type; template or ad-hoc:

    -   For template based document tracking, create a **user policy** object passing the license metadata as a parameter.

        For more information, see [**UserPolicy.create**](userpolicy-create-templatedescriptor-method-java.md) and [**MSUserPolicy.userPolicyWithTemplateDescriptor**](msuserpolicy-protectionpolicywithtemplatedescriptor-userid-authenticationcallback-options-completionblock-method-objc.md).

    -   For ad-hoc based document tracking, set the **license metadata** property on the **policy descriptor** object.

        For more information, see [**PolicyDescriptor.getLicenseMetadata**](policydescriptor-getlicensemetadata-java.md), [**PolicyDescriptor.setLicenseMetadata**](policydescriptor-setlicensemetadata-java.md) and [**MSPolicyDescriptor.licenseMetadata**](mspolicydescriptor-licensemetadata-property-objc.md).

    > [!Note]  
    > The license metadata object is only directly accessible during the process of setting up document tracking for the given user policy. Once the user policy object is created, the associated license metadata is not accessible i.e. changing the values of licence metadata has no effect.

     

-   Call the platform registration method for document tracking.

    See [**MSUserPolicy.registerForDocTracking**](msuserpolicy-registerfordoctracking-userid-authenticationcallback-completionblock-method-objc.md) or [**UserPolicy.registerForDocTracking**](userpolicy-registerfordoctracking-boolean--sting--authenticationcallback--creationcallback--java.md).

 

 




