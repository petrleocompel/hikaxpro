# Changelog

## v2.3.1
- **fix**: stop unbounded 401 reconnect recursion when re-auth fails (hikaxpro_hacs#212)
- **fix**: null-safe `connect()` when session capabilities are unavailable
- **fix**: keep only the `WebSession` cookie value from `Set-Cookie` (drop Path/HttpOnly attributes)

## v2.3.0
- **feat**: add `X-Userlevel` header to specify user type
- **chore**: dependency upgrade (minor)

## v2.2.1
- **feat**: add more endpoint constants (`OutputControl`)

## v2.2.0
- **feat**: add support for more endpoint constants
- **feat**: add support for session login version 2.0

## v2.1.3
- **fix**: SessionLogin model XML (attribute names), parsing irreversible attribute (#1)

## v2.1.2
- **fix**: add missing zones endpoint constant

## Earlier
See git history for releases before structured changelog entries.
