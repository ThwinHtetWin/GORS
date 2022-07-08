# GORS
GitHub Organization Repos Scanner

How this works - 
1. This tool collects the git repos of the user provided organization's sources (which are not forked by the organization) and are public.
2. Then we use [Trufflehog](https://github.com/trufflesecurity/trufflehog) to find leaked credentials. 

## Requirements
1. You need to install [Trufflehog](https://github.com/trufflesecurity/trufflehog) at /usr/bin/.
