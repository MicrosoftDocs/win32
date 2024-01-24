---
title: OneX schema elements
description: An 802.1X profile contains the following schema elements.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- Schema
api_location: 
ms.assetid: be3f1986-d0c2-47f6-b4dd-8defb89bd03a
---

# OneX schema elements

An 802.1X profile contains the following schema elements. All OneX schema elements apply to both wired and wireless profiles. Most of the named elements are in the namespace `https://www.microsoft.com/networking/OneX/v1`, except for [**EAPConfig (OneX)**](onexschema-onex-element.md#eapconfig) which is in the namespace `https://www.microsoft.com/provisioning/EapHostConfig`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## All elements

* [**OneX**](./onexschema-onex-element.md)
  * [**cacheUserData (OneX)**](./onexschema-onex-element.md#cacheuserdata)
  * [**heldPeriod (OneX)**](./onexschema-onex-element.md#heldperiod)
  * [**authPeriod (OneX)**](./onexschema-onex-element.md#authperiod)
  * [**startPeriod (OneX)**](./onexschema-onex-element.md#startperiod)
  * [**maxStart (OneX)**](./onexschema-onex-element.md#maxstart)
  * [**maxAuthFailures (OneX)**](./onexschema-onex-element.md#maxauthfailures)
  * [**supplicantMode (OneX)**](./onexschema-onex-element.md#supplicantmode)
  * [**authMode (OneX)**](./onexschema-onex-element.md#authmode)
  * [**singleSignOn (OneX)**](./onexschema-singlesignon-onex-element.md)
    * [**type (singleSignOn)**](./onexschema-singlesignon-onex-element.md#type)
    * [**maxDelay (singleSignOn)**](./onexschema-singlesignon-onex-element.md#maxdelay)
    * [**allowAdditionalDialogs (singleSignOn)**](./onexschema-singlesignon-onex-element.md#allowadditionaldialogs)
    * [**maxDelayWithAdditionalDialogs (singleSignOn)**](./onexschema-singlesignon-onex-element.md#maxdelaywithadditionaldialogs)
    * [**userBasedVirtualLan (singleSignOn)**](./onexschema-singlesignon-onex-element.md#userbasedvirtuallan)
  * [**EAPConfig (OneX)**](./onexschema-onex-element.md#eapconfig)
