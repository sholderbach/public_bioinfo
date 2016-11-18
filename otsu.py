def otsu(hist):
    left = list()
    right = list()
    score = list()
    n = len(hist)
    for i in range(1,n):
        left = hist[:i]
        right = hist[i:]
        m_left = sum([j*hist[j] for j in range(i)])/sum(left)
        m_right = sum([j*hist[j] for j in range(i,n)])/sum(right)
        v_left = sum([((j-m_left)**2)*hist[j] for j in range(i)])/sum(left)
        v_right = sum([((j-m_right)**2)*hist[j] for j in range(i,n)])/sum(right)
        s = v_left*sum(left) + v_right*sum(right)
        print("Threshold = "+ str(i-1)+" --> Score = "+str(s))
        score.append(s)
    threshold = min(enumerate(score), key = lambda p: p[1])
    return threshold[0]

histogram = [1,6,3,1,1,2,1]
print("T = " + str(otsu(histogram)))
