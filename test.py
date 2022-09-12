# %%
from ast import If
import json
from operator import itemgetter
from collections import Counter


# %%
with open("C:/Users/baldw/Documents/..DSS/DSS_S22_Reddit/raw_data/dat1.json", "r") as read_file:
    data = json.load(read_file)

type(data)
# %%

len(data)

itemgetter(['data'])(data)


# %%

# defines more as total number of comments in Reddit thread
more = data['data']['submission_metadata']['num_comments']
# defines post as Reddit comment reply
com = data['data']
par = data['data']['comments']


# %%

def reddit_com(com):
    for i in range(len(data['data']['comments'])):
        # print('Author: {} \n {}'.format(i['author'], i['body']))
        print('\n Parent Comment {} Author:'.format(
            i), data['data']['comments'][i]['author'])
        print('\n Parent Comment {}:'.format(i),
              data['data']['comments'][i]['body'])

        # x = 0
        # if x in data['data']['comments'][x]['replies']:
        #   print(x), 'Child Comment {}:'.format(
        #      data['data']['comments'][x]['replies'])
        # reddit_rep(post)
        # x += 1
        # if len(com[i]['comments']) >= 0:
        #    com = com[i]['comments']
        #    reddit_com(com)


def reddit_rep(post):
    print('Child Comment:', data['data']['comments']['replies']['body'])

    # for i in range(0, len(post)):
    #    print('Child Comment {}'.format(i), post[i]['body'])
    #    print('\n')
    #    if len(post[i]['replies']) > 0:
    #        post = post[i]['replies']
    #        reddit_rep(post)

# first print prints title of Reddit post

# first for loop prints all original parents without chilren (replies)

# second for loop will give full thread from first parent then end


Counter([k['comments'] for k in data if k.get('body')])


def reddit_study(more):
    print('Original Post Author:', data['data']
          ['submission_metadata']['author'], '\n')
    print('Original Post: \n', data['data']['submission_metadata']['title'])
    print("\n")
    nomore = data['data']['submission_metadata']['num_comments']
    print('TOTAL COMMENTS {}'.format(nomore))
    again = 0
    parent = range(len(data['data']['comments']))
    while again <= nomore:
        for i in parent:
            print('\n Parent Comment {} Author:'.format(
                i), data['data']['comments'][i]['author'])
            print('\n Parent Comment {}:'.format(i),
                  data['data']['comments'][i]['body'])
            again += 1
            child = range(len(data['data']['comments']['replies']))
            print('CHILD COMMENT:')
            print(len(data['data']['comments']['replies'][i]['body']))
            if 'replies' not in child:  # Begin test code
                child['replies'] = -1
                please = int(data(['data']['comments']['replies'][i]['body']))
                print(please)
# OLD CODE BELOW

            for i in child:
                print('Child Comment:', data['data']
                      ['comments'][int(i)]['replies']['body'])
                again += 1
            print("PARENT COMMENT {}".format(again))
        # if j in range(len(com[i])) <= more:
        # reddit_com(com)
        print(again)
        # again += 1
        # parent += 1
        #
        # if i['data']['comments']#['replies'] > 0:
        #    reddit_rep(post)
        # j += 1
    reddit_study(more)

# more test code below
      k = hasattr(data, 'body')
       if k == True:
            getattr(data, 'body')
        print(again)
        again += 1
        parent += 1

reply_dict = 'replies' in data
reply_dict

# %%
reddit_com(post)

# %%
