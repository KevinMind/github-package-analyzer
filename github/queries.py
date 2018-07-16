

# query for the first 100 repos for search 'react starter... just the urls...
get_100_githubs = """
{
    search(first: 100, type: REPOSITORY, query: "react starter") {
        repositoryCount
        pageInfo {
          hasNextPage
        }
        edges {
          node {
            ... on Repository {
              url
            }
          }
        }
    }
}
"""
