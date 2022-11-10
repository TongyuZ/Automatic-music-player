# PLAYLIST = ["Old MacDonald", "Row Your Boat", "Happy"]
# SONGS = [ ['old macdonald had a farm - ee-i-ee-i-o.',
#         'and on that farm he had a cow - ee-i-ee-i-o.',
#         'with a moo moo here and a moo moo there',
#         'here a moo - there a moo - everywhere a moo moo',
#         'old macdonald had a farm - ee-i-ee-i-o.' ],
#
#          ['row row row your boat',
#         'gently down the stream.',
#         'merrily merrily merrily merrily',
#         'life is but a dream' ],
#
#          ['huh, because i\'m happy',
#           'clap along if you feel like a room without a roof',
#           'because i\'m happy',
#           'clap along if you feel like happiness is the truth',
#           'because i\'m happy',
#           'clap along if you know what happiness is to you',
#           'because i\'m happy',
#           'clap along if you feel like that\'s what you wanna do']]

def longestConsecutive(nums) -> int:
    max_num = 0
    c = [0] * len(nums)
    for i in range(len(nums)):
        n = nums[i]
        l = n - 1
        r = n + 1
        c[i] = c[i] + 1
        while l in nums:
            l = l - 1
            c[i] = c[i] + 1
        while r in nums:
            r = r + 1
            c[i] = c[i] + 1
    for j in range(len(c)):
        max_num = max(max_num, c[j])
    return max_num
print(longestConsecutive([100,200,300,301,302,700]))