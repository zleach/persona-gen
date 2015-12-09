{% for experiment in experiments %}
  <div class="card experiment">
    <div class="card-top ">
    </div>
    <div class="card-content">
      <div class="card-bottom">
        <h3>{{ experiment.name }}</h3>
        <span class="badge pull-right skill-value">{{ experiment.skillValue }}</span>
        <h4 class="archetype">Experiment</h4>
        
        <ul class="skills">
        {% for skill in experiment.skills %}
          <li>
          {{ skill.name }}
          <span class="level-amount text-muted">{{ skill.level }}</span>
          <div class="level row-{{loop.index}}">
            <div {%if skill.level > 0 %} class="filled" {% endif %}></div><div {%if skill.level > 1 %} class="filled" {% endif %}></div><div {%if skill.level > 2 %} class="filled" {% endif %}></div><div {%if skill.level > 3 %} class="filled" {% endif %}></div><div {%if skill.level > 4 %} class="filled" {% endif %}></div></div>
          </li>
        {% endfor %}
        </ul>

        <span class="badge pull-right experiment-value"><small>$</small>{{ experiment.resultValue }}</span>
        
      </div>
    </div>
  </div>
{% endfor %}



{% for person in people %}
  <div class="card">
    <div class="card-content">
      <div class="card-top" style="background-color: #{{ person.avatar.backgroundColor }}">
        <div class="avatar" style="background-image: url('{{ person.avatar.url }}');"></div>
      </div>
      {# <div class="face" style="background-image: url('static/img/{{ person.image }}');"></div> #}
      <div class="card-bottom">
        <h3 class="person-name">{{ person.fullName }}</h3>
        <span class="badge pull-right skill-value person-skill-value" style="background-color: #{{ person.avatar.backgroundColor }}"><small>$</small>{{ person.skillValue }}</span>
        <h4 class="archetype">{{ person.archetype }}</h4>
        <h4 class="person-title text-muted">{{ person.title }} {# at {{ person.company }} #}</h4>
        
        {# <p><b>Skills ({{ person.skillValue }})</b></p> #}
        <ul class="skills">
        {% for skill in person.skills %}
          <li>
          <div class="level row-{{loop.index}}  {% if skill.level == 0 %}no-skill{% endif %}">
            <div class="filled dot">{{ skill.level }}</div>
            <span class="skill-name">{{ skill.name }}</span>
          </div>
          </li>
        {% endfor %}
        </ul>


{#
        {% for skill in person.skills %}
          <li>
          {{ skill.name }}
          <span class="level-amount text-muted">{{ skill.level }}</span>
          <div class="level row-{{loop.index}}">
            <div {%if skill.level > 0 %} class="filled" {% endif %}></div><div {%if skill.level > 1 %} class="filled" {% endif %}></div><div {%if skill.level > 2 %} class="filled" {% endif %}></div><div {%if skill.level > 3 %} class="filled" {% endif %}></div><div {%if skill.level > 4 %} class="filled" {% endif %}></div></div>
          </li>
        {% endfor %}

        <p><b>Successful Lone Wolves Can</b></p>
        <ul>
          <li>Easily generate test ideas that are specific to their industry and match wider company objectives.            </li>
          <li>Execute tests with minimum help from developers.                                                              </li>
          <li>Synthesize test results into digestible reports and presentations of varying levels of detail.                </li>
          <li>Quickly and easy describe A/B testing and its benefits to any audience.                                       </li>
          <li>Demonstrate shifts in KPIs to expand testing culture within the company and increase resources for their team.</li>
          <li>Create a highly organized system to track information about multiple tests over time.                         </li>
        </ul>

        <p><b>Testing maturity level at company</b></p>
        <ul>
          <li>Interested</li>
        </ul>

        <p><b>Main Motivation</b></p>
        <ul>
          <li>To quickly and easily run successful tests and expand a fledgling A/B testing culture</li>
        </ul>

        <p><b>Top Frustration</b></p>
        <ul>
          <li>Lone wolves lack the time, dedicated people resources, and internal support to design and implement the most robust tests.</li>
        </ul>

Percentage of time spent on:
A/B Testing 20%
Other Work 60%
Using Optimizely 20%
 #}

      </div>
    </div>
  </div>
{% endfor %}


