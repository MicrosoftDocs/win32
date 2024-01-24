---
description: The concept of an address is core to most communications operations.
ms.assetid: 32fbd06b-f6f2-4024-b8d5-3d6eef16bca2
title: Address
ms.topic: article
ms.date: 05/31/2018
---

# Address

The concept of an address is core to most communications operations. An address represents a location on a network. The local assignment of an address to a line or channel typically takes place during the installation of the service provider but can be modified later. Details on the procedures involved can be found in the operating system's Resource Kit for Microsoft-supplied service providers and in the service provider documentation for non-Microsoft products.

A single address may be shared by more than one line device. Different switch vendors have different names for this concept, such as address bridging, multiple appearance directory number (MADN), or bridged appearance. An incoming call on a shared address is offered on all lines associated with the address. See [LINEADDRESSSHARING\_ Constants](./lineaddresssharing--constants.md) for a description of the configurations that TAPI recognizes.

The address itself is a string that identifies a location on a network. In the case of a telephone network, the address is a telephone number complete with national or international codes. If the network is IP-based, the address may be an IP address. See [LINEADDRESSTYPE\_ Constants](lineaddresstype--constants.md) for TAPI-defined address types. A service provider may define additional address types.

## Address-Related Capabilities and Messages

Different addresses have different features, capabilities, and states. The service providers are the source of such information. TAPI's device-query capability and status and event-reporting mechanisms give an application the information to manage addresses.

Applications acquire this information by processing events from TAPI or by using query operations. This allows an application to take into account factors such as whether a given address supports a specific capability, such as [park](park-ovr.md).

**TAPI 2.x:** Applications call the [**lineGetAddressCaps**](/windows/win32/api/tapi/nf-tapi-linegetaddresscaps) function to determine the telephony capabilities of each address and then receives this information in a [**LINEADDRESSCAPS**](/windows/win32/api/tapi/ns-tapi-lineaddresscaps) data structure. In a similar way, an application can call [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps) for a line device to determine the number of addresses assigned to the line, as well as other information.

**TAPI 3.x:** Applications use the [Address Object Interfaces](address-object-interfaces.md) to acquire information on address capabilities and events.

## Storing Phone Numbers in Electronic Address Books

Many users choose to dial people, fax machines, bulletin boards, and other entities by selecting their names from an address book. The actual number dialed depends on the geographic location of the user and the way the line device to be used is connected. For example, a desktop computer can have access to two lines, one connected to a PBX, the other to the telephone company's central office. When making a call to the same party, different numbers may have to be used. (To dial through the PBX, for example, the computer may need to dial a "9" prefix to get an outside line, or a different prefix may be needed for a call made through the central office.) Or, a user may make calls from a portable computer and want to use a single, static address book even when calling from different locations or telephony environments. TAPI's address translation capabilities let the user inform the computer of the current location and the desired line device for the call. TAPI then handles any dialing differences, requiring no changes to the user's address book. An application uses [address translation](initiate-a-session-ovr.md) to convert an address from the [canonical address](#canonical-addresses) format to the [dialable address](#dialable-addresses) format.

A related topic is the handling of international call-progress monitoring, which is the process of listening for audible tones such as dial tone, special information tones, busy signals, and ringback tones to determine the *state* of a call (its progress through the network). Because the cadences and frequencies of call-progress tones vary from country or region to country or region, the service provider must know what call progress to follow when making an international outgoing call. Therefore, applications specify the destination country or region code when placing outgoing calls.

## Canonical Addresses

The canonical address format is intended to be a universally constant directory number. For this reason, numbers in address books are best stored using canonical format.

The following details concern what is considered canonical for a phone address.

A canonical phone address is a text string with the following structure:

\+ *CountryCode* Space \[**(***AreaCode***)** Space\] *SubscriberNumber* \| *Subaddress* ^ *Name* CRLF ...

The components of this structure are described in the following table.



Component

Meaning

\+

Equivalent to hex 2B. Indicates that the number that follows it uses the canonical format.

*CountryCode*

A variably sized string containing one or more of the digits "0" through "9" (hex 30 through 39, inclusive). The *CountryCode* is delimited by the following Space. It identifies the country or region in which the address is located.

Space

Exactly one space character (hex 20). It is used to delimit the end of the *CountryCode* part of an address.

*AreaCode*

A variably sized string containing zero or more of the digits "0" through "9" (hex 30 through 39, inclusive). *AreaCode* is the area code part of the address and is optional. If the area code is present, it must be preceded by exactly one left parenthesis character (28), and be followed by exactly one right parenthesis character (29) and one space character (20).

*SubscriberNumber*

A variably sized string containing one or more of the digits "0" through "9" (hex 30 through 39, inclusive). It may include other formatting characters as well, including any of the dialing control characters described in the Dialable Address Format:

 

Character

Hex encoding

 

! \#<br/> $<br/> \*<br/> ,<br/> ?<br/> @<br/> ABCD<br/> P<br/> T<br/> W<br/> abcd<br/> p<br/> t<br/> w<br/>

21 23<br/> 24<br/> 2A<br/> 2C<br/> 3F<br/> 40<br/> 41-44<br/> 50<br/> 54<br/> 77<br/> 61-64<br/> 70<br/> 74<br/> 79<br/>

 

The subscriber number should not contain the left parenthesis or right parenthesis character (which are used only to delimit the area code), nor should it contain the "\|", "^", or CRLF characters (which are used to begin following fields). Most commonly, nondigit characters in the subscriber number would include only spaces, periods ("."), and dashes ("-"). Any allowable nondigit characters that appear in the subscriber number are omitted from the *DialableString* returned by the [**lineTranslateAddress**](/windows/win32/api/tapi/nf-tapi-linetranslateaddress) function, but are retained in the *DisplayableString*.

\|

Hex (7C). If this optional character is present, the information following it up to the next + \| ^ CRLF, or the end of the canonical address string, is treated as subaddress information, as for an ISDN subaddress.

*Subaddress*

A variably sized string containing a subaddress. The string is delimited by + \| ^ CRLF or the end of the address string. During dialing, subaddress information is passed to the remote party. It can be such things as an ISDN subaddress or an e-mail address.

^

Hex (5E). If this optional character is present, the information following it up to the next CRLF or the end of the canonical address string is treated as an ISDN name.

*Name*

A variably sized string treated as name information. Name is delimited by CRLF or the end of the canonical address string and can contain other delimiters. During dialing, name information is passed to the remote party.

CRLF

Hex (0D) followed by Hex (0A), and is optional. If present, it indicates that another canonical number is following this one. It is used to separate multiple canonical addresses as part of a single address string (inverse multiplexing). For example, the canonical representation of the main switchboard telephone number at Microsoft Corporation would be:<br/> +1 (425) 882-8080<br/>



 

## Dialable Addresses

The dialable address format is the form in which an address is passed to a service provider that handles telephone numbers. The following details concern dialable addresses on a phone network.

The dialable number format allows multiple destination addresses to be supplied at once. This ability can be useful if the service provider offers some form of inverse multiplexing by setting up calls to each of the specified destinations and then managing the information stream as a single high-bandwidth media stream. The application perceives this group of calls as a single call because it receives only a single call handle representing the aggregate of the individual phone calls.

It is also possible to support inverse multiplexing at the application level. To do this, the application would set up a series of individual calls and synchronize their media streams.

*Subaddressing* is a capability provided on ISDN lines that allows more information than just a single telephone number to be used when dialing. This additional information can specify an individual telephone extension to ring or, in a computing environment, a particular application to be alerted. Other parameters can describe the required aspects of a requested connection, such as rate and timing.

If subaddressing is supported by a service provider, the application includes this in the address passed to any operation that requires one.

A dialable phone address contains part addressing information and is part navigational in nature. Any input string that does not begin with a "+" character is presumed not to be in canonical format and therefore to be in dialable address format, and is returned to the application unmodified. A dialable address is a text string with the following structure:

*DialableNumber* \| *Subaddress* ^ *Name* CRLF ...

The components of this structure are given in the following table.



| Component        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *DialableNumber* | Digits and modifiers 0-9 A-D \* \# , ! W w P p T t @ $ ? ; delimited by \| ^ CRLF or the end of the dialable address string. The plus sign (+) is a valid character in dialable strings. It indicates that the phone number is a fully qualified international number. Within the *DialableNumber*, note the following definitions:<br/> 0-9 A-D \* \#<br/> Characters corresponding to the DTMF and/or pulse digits.<br/> |
| !                | Hex (21). Indicates that a hookflash (one-half second onhook, followed by one-half second offhook before continuing) is to be inserted in the dial string.                                                                                                                                                                                                                                                                                   |
| P p              | Hex (50) or Hex (70). Indicates that pulse dialing is to be used for the digits following it.                                                                                                                                                                                                                                                                                                                                                |
| T t              | Hex (54) or Hex (74). Indicates that tone (DTMF) dialing is to be used for the digits following it.                                                                                                                                                                                                                                                                                                                                          |
| ,                | Hex (27). Indicates that dialing is to be paused. The duration of a pause is device specific and can be retrieved from the line's device capabilities. Multiple commas can be used to provide longer pauses.                                                                                                                                                                                                                                 |
| W w              | Hex (57) or Hex (77). An uppercase or lowercase W indicates that dialing should proceed only after a dial tone has been detected.                                                                                                                                                                                                                                                                                                            |
| @                | Hex (40). Indicates that dialing is to "wait for quiet answer" before dialing the remainder of the dialable address. This means to wait for at least one ringback tone followed by several seconds of silence.                                                                                                                                                                                                                               |
| $                | Hex (24). Indicates that dialing the billing information is to wait for a "billing signal" (such as a credit card prompt tone).                                                                                                                                                                                                                                                                                                              |
| ?                | Hex (3F). Indicates that the user is to be prompted before continuing with dialing. The provider does not actually do the prompting, but the presence of the "?" forces the provider to reject the string as invalid, alerting the application to the need to break it into pieces and prompt the user in-between.                                                                                                                           |
| ;                | Hex (3B). If placed at the end of a partially specified dialable address string, it indicates that the dialable number information is incomplete and more address information will be provided later. The ";" component is only allowed in the *DialableNumber* portion of an address.                                                                                                                                                       |
| \|               | Hex (7C), and is optional. If present, the information following it up to the next + \| ^ CRLF, or the end of the dialable address string is treated as subaddress information (as for an ISDN subaddress).                                                                                                                                                                                                                                  |
| *Subaddress*     | A variably sized string containing a subaddress. The string is delimited by the next + \| ^ CRLF or the end of the address string. When dialing, subaddress information is passed to the remote party. It can be for an ISDN subaddress, an e-mail address, and so on.                                                                                                                                                                       |
| ^                | Hex (5E), and is optional. If present, the information following it up to the next CRLF or the end of the dialable address string is treated as an ISDN name.                                                                                                                                                                                                                                                                                |
| *Name*           | A variably sized string treated as name information. Name is delimited by CRLF or the end of the dialable address string. When dialing, name information is passed to the remote party.                                                                                                                                                                                                                                                      |
| CRLF             | Hex (0D) followed by Hex (0A). If present, this optional character indicates that another dialable number is following this one. It is used to separate multiple dialable addresses as part of a single address string (for inverse multiplexing).                                                                                                                                                                                           |



 

Address translation can be used to translate an address from canonical format to dialable format.

 

