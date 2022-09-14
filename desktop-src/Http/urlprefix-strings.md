---
title: UrlPrefix Strings
description: In the HTTP Server API, a UrlPrefix is a wide-character (UTF-16) Unicode string with a canonical form that specifies a section of URL namespace.
ms.assetid: 4f317bf6-ee6a-47a8-a531-78534217109d
keywords:
- UrlPrefix strings HTTP Server API
ms.topic: article
ms.date: 05/31/2018
---

# UrlPrefix Strings

In the HTTP Server API, a *UrlPrefix* is a wide-character (UTF-16) Unicode string with a canonical form that specifies a section of URL namespace. It is used to reserve a section of URL namespace for a user account or register a section of URL namespace for a process.

## UrlPrefix Format

A UrlPrefix has the following syntax:

"scheme://host:port/relativeURI"

The scheme, host and port elements of a UrlPrefix must be present and non-empty, and must obey the following rules:

<dl> <dt>

<span id="scheme"></span><span id="SCHEME"></span>scheme
</dt> <dd>

Must be either http or https, all in lowercase.

</dd> <dt>

<span id="host"></span><span id="HOST"></span>host
</dt> <dd>

Must be a fully qualified domain name, an IPv4 or IPv6 literal string, or a wildcard. Unlike the scheme, which must be lowercase, the host portion is case-insensitive. Depending on how its host portion is specified, a UrlPrefix falls into one of the following four routing categories, which are described in more detail below:

<dl> <dd>Strong wildcard</dd> <dd>Explicit</dd> <dd>IP-bound weak wildcard</dd> <dd>Weak wildcard</dd> </dl> </dd> <dt>

<span id="port"></span><span id="PORT"></span>port
</dt> <dd>

A decimal numeric string that does not start with zero and that represents a valid TCP port number (1 to 65,535). This value cannot be a wildcard.

</dd> <dt>

<span id="relativeURI"></span><span id="relativeuri"></span><span id="RELATIVEURI"></span>relativeURI
</dt> <dd>

The relativeURI element is optional, but if present must always be followed by a slash character ("/"). This is a prefix string that indicates a subtree within the machine's namespace specified relative to the scheme, host and port values. Unlike the scheme, which must be lowercase, the relativeURI portion is case-insensitive.

</dd> </dl>

Examples of properly formed UrlPrefixes are:

-   `https://www.adatum.com:80/vroot/`
-   `https://adatum.com:443/secure/database/`
-   `https://+:80/vroot/`

## Host-Specifier Categories

For flexibility and ease of use, the HTTP Server API supports four different ways to specify hosts. The four host-specifier categories are listed below in order of precedence:

<dl> <dt>

<span id="Strong_wildcard__Plus_Sign_"></span><span id="strong_wildcard__plus_sign_"></span><span id="STRONG_WILDCARD__PLUS_SIGN_"></span>Strong wildcard (Plus Sign)
</dt> <dd>

When the host element of a UrlPrefix consists of a single plus sign (+), the UrlPrefix matches all possible host names in the context of its scheme, port and relativeURI elements, and falls into the strong wildcard category.

A strong wildcard is useful when an application needs to serve requests addressed to one or more relativeURIs, regardless of how those requests arrive on the machine or what site they specify in their Host headers. Use of a strong wildcard in this situation avoids the need to specify an exhaustive list of host and/or IP-addresses.

</dd> <dt>

<span id="Explicit"></span><span id="explicit"></span><span id="EXPLICIT"></span>Explicit
</dt> <dd>

An explicit host name such as a fully qualified domain name in the host element places a UrlPrefix in the explicit category. This kind of host element is matched directly against the Host headers of incoming requests.

Explicit host specifications are useful for multi-site applications such as Web servers that deliver different content depending on the site to which the request was directed.

</dd> <dt>

<span id="IP-bound_weak_wildcard"></span><span id="ip-bound_weak_wildcard"></span><span id="IP-BOUND_WEAK_WILDCARD"></span>IP-bound weak wildcard
</dt> <dd>

When an IP address appears as the host element, then the UrlPrefix falls into the IP-bound Weak Wildcard category. This kind of UrlPrefix matches any host name for the specified IP interface with the specified scheme, port and relativeURI, and that has not already been matched by a strong-wildcard or explicit UrlPrefix. The IP address takes one of two forms in the host element:

<dl> <dt>

<span id="IPv4_Literal_String"></span><span id="ipv4_literal_string"></span><span id="IPV4_LITERAL_STRING"></span>IPv4 Literal String
</dt> <dd>

An IPv4 literal consists of four dotted decimal numbers, each in the range 0-255, such as 192.168.0.0.

</dd> <dt>

<span id="IPv6_Literal_String"></span><span id="ipv6_literal_string"></span><span id="IPV6_LITERAL_STRING"></span>IPv6 Literal String
</dt> <dd>

An IPv6 literal string is enclosed in square brackets and contains hex numbers separated by colons; for example: \[::1\] or \[3ffe:ffff::6ECB:0101\].

</dd> </dl>

IP-bound weak-wildcard host specifiers are intended for applications that vary the content they serve based on the route taken by incoming requests. Do not rely on IP-bound weak-wildcard host specifiers to enforce security.

</dd> <dt>

<span id="Weak_wildcard__asterisk_"></span><span id="weak_wildcard__asterisk_"></span><span id="WEAK_WILDCARD__ASTERISK_"></span>Weak wildcard (asterisk)
</dt> <dd>

When an asterisk (\*) appears as the host element, then the UrlPrefix falls into the weak wildcard category. This kind of UrlPrefix matches any host name associated with the specified scheme, port and relativeURI that has not already been matched by a strong-wildcard, explicit, or IP-bound weak-wildcard UrlPrefix.

This host specification can be used as a default catch-all in some circumstances, or can be used to specify a large section of URL namespace without having to use many UrlPrefixes.

</dd> </dl>

## UrlPrefix Conflict Detection During Reservation and Registration

For reservation and registration purposes, the four different categories of UrlPrefix are treated separately, without reference to one another. It is possible to register conflicting UrlPrefixes as long as they are in different categories. Only within the same category does a conflict cause a reservation attempt to fail.

For example, it would be possible to reserve both the explicit UrlPrefix `https://www.adatum.com:80/vroot/` and the conflicting strong wildcard UrlPrefix `https://+:80/vroot/`, since they belong to different categories. However, a subsequent attempt to reserve https://+:80/vroot/ to a different user would fail because it would conflict with an existing reservation in its own category.

## Routing Behavior

When routing an incoming HTTP request, the HTTP Server API starts with the strong wildcard category and compares the incoming URL with both registered and reserved UrlPrefixes in that category.

If the incoming URL matches a reservation but not a registration, the HTTP Server API fails the request. This prevents a lower-priority registrations from being able to pick up requests not intended for it. The status on failure is 400 ("Bad Request") rather than 503 ("Service not available"), because a 503 return is sometimes mistakenly interpreted by load-balancing gateways as indicating that the server was overloaded.

If a matching registration is found within the category, the request is routed to the request queue associated with that registration. The request is always routed to the queue associated with the longest matching UrlPrefix within a category.

If no match is found in the category, then the HTTP Server API proceeds to the explicit category and repeats the same procedure. To summarize, the order in which the categories are examined is as follows:

1.  Strong wildcard
2.  Explicit
3.  IP-Bound weak wildcard
4.  Weak wildcard

If no match is found in any of the categories, the HTTP Server API sends a response with a status code of 400 to indicate that the request cannot be routed.

## Longest Match Rule

Within each UrlPrefix category, HTTP Server API routes a request to the queue associated with the longest matching UrlPrefix. For example, suppose the following two UrlPrefixes are registered to different queues:

- `Queue1 https://www.adatum.com:80/`
- `Queue2 https://www.adatum.com:80/dir/sna/`

The HTTP Server API routes a request for `https://www.adatum.com:80/default.htm` to Queue1, and a request for `https://www.adatum.com:80/dir/sna/snadefault.htm` to Queue2. It routes a request for `https://www.adatum.com:80/dir/app.htm` to Queue1 because the longest complete match is with the `https://www.adatum.com:80/` UrlPrefix, not with the `https://www.adatum.com:80/dir/sna` UrlPrefix.

 

 




