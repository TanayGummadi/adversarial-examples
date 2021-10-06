import os
import pandas

cdn_url="https://ghcdn.rawgit.org/CloakCam/adversarial-examples/"
tag="15c5efe9d25cf2a1eb42a8fbeed538ccf8f3caed"

def build_table(dir, extension):
  df = pandas.DataFrame(os.listdir(os.path.join('./', dir)), columns=['name'])
  df[dir] = [os.path.join(cdn_url, tag, dir, a) for a in df['name']]
  df['name'] = df['name'].str.replace(extension,'')
  df = df.set_index('name')
  print(df.head())
  return df


def merge_dfs(source_dict):
  # Build originals table
  df = build_table('original', '.jpg')
  for key, value in source_dict.items():
    # Build originals table
    df = df.merge(build_table(key, value), on='name')
  return df

def main():
  sources = {'lowkey': '.png', 'fawkes/high': '.png', 'fawkes/mid': '.png', 'fawkes/low': '.png', 'colorfilter': '.jpg'}
  df = merge_dfs(sources)
  df.to_json('urls.json')

if __name__ == "__main__":
  main()
